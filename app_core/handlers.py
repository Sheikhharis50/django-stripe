from django.conf import settings
import stripe

from app_subscription.functions import create_user_subscription


class StripeEventHandler:
    def __init__(self, payload, sig_header) -> None:
        self.payload = payload
        self.signature = sig_header

    def create_event(self):
        try:
            self.event = stripe.Webhook.construct_event(
                self.payload,
                self.signature,
                settings.STRIPE_WEBHOOK_KEY,
            )
            return True
        except ValueError as e:
            # Invalid payload
            print(e)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            print(e)
        return False

    def execute_event(self):
        try:
            event_type = self.event.get("type")
            if event_type == "checkout.session.completed":
                self._checkout_session_completed()
            elif event_type == "checkout.session.async_payment_succeeded":
                self._checkout_session_payment_succeeded()
            elif event_type == "checkout.session.async_payment_failed":
                self._checkout_session_payment_failed()
        except Exception as e:
            print(e)

    def _checkout_session_completed(self):
        session = self.event["data"]["object"]
        print("`_checkout_session_completed`: ", session)

        if session.payment_status == "paid":
            self._checkout_fulfillment(session)

    def _checkout_session_payment_succeeded(self):
        session = self.event["data"]["object"]
        print("`_checkout_session_payment_succeeded`: ", session)
        self._checkout_fulfillment(session)

    def _checkout_session_payment_failed(self):
        session = self.event["data"]["object"]
        print("`_checkout_session_payment_failed`: ", session)

        # notify user that his subscription payment is failed.

    def _checkout_fulfillment(self, session):
        metadata = session["metadata"]

        user_id = metadata.get("user_id")
        subscription_id = metadata.get("subscription_id")

        create_user_subscription(
            dict(
                subscription_id=subscription_id,
                user_id=user_id,
                transaction_data=session,
            ),
            payment_confirm=True,
        )

        # notify user that his subscription is made.
