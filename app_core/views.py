from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from http import HTTPStatus
import random
import stripe

from app_core.response import Response
from app_core.handlers import StripeEventHandler
from app_subscription.models import Subscription


class LandingView(TemplateView):
    template_name = "pages/landing.html"

    def map_colors(self, queryset):
        colors = ("#325288", "#750550", "#35858B", "#470D21", "#072227", "#35858B")

        def add_color(instance):
            setattr(instance, "color", random.choice(colors))
            return instance

        return list(map(add_color, queryset))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subscriptions"] = self.map_colors(Subscription.objects.all())
        return context


class CreateCheckoutSessionView(View):
    def get_subscription(self, subscription_id):
        return Subscription.objects.get(id=subscription_id)

    def post(self, request, subscription_id, **kwargs):
        try:
            subscription = self.get_subscription(subscription_id)
            checkout_session = stripe.checkout.Session.create(
                api_key=settings.STRIPE_SECRET_KEY,
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "unit_amount_decimal": subscription.price,
                            "product_data": {
                                "name": subscription.name,
                            },
                        },
                        "quantity": 1,
                    },
                ],
                metadata={
                    "subscription_id": subscription_id,
                    "user_id": request.user.id,
                },
                mode="payment",
                success_url=f"{settings.ENDPOINT}/subscription/{subscription_id}/success",
                cancel_url=f"{settings.ENDPOINT}/subscription/{subscription_id}/cancel",
            )
        except Exception as e:
            print(e)
            return Response(status=HTTPStatus.FORBIDDEN)
        return redirect(checkout_session.url, code=303)


@method_decorator(csrf_exempt, name="dispatch")
class StripeWebhookView(View):
    def post(self, request):
        payload = request.body
        signature = request.META["HTTP_STRIPE_SIGNATURE"]
        handler = StripeEventHandler(payload, signature)

        handler.create_event()

        # Handle the checkout.session.completed event
        handler.execute_event()

        return Response()
