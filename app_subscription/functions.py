from app_subscription.models import (
    UserSubscription,
)
from utils.enums import PaymentStatus


def create_user_subscription(data, payment_confirm=False):
    try:
        if payment_confirm:
            data["payment_status"] = PaymentStatus.PAID.value
        return UserSubscription.objects.create(**data)
    except Exception as e:
        print(e)
    return None
