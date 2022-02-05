from django.db import models, transaction
from django.core import exceptions

from app_core.forms import ModelForm
from app_order.models import Order
from app_subscription.models import UserSubscription


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["user", "description"]

    def clean_user(self):
        user = self.cleaned_data.get("user")
        if (
            not UserSubscription.objects.select_related("subscription")
            .filter(user=user, ordered__lt=models.F("subscription__can_order"))
            .exists()
        ):
            raise exceptions.ValidationError(
                f"{user.get_full_name()} has no subscription to make an order."
            )
        return user

    @transaction.atomic
    def save(self, commit: bool):
        instance = super().save(commit)

        user_sub = UserSubscription.objects.filter(user=instance.user).order_by("-id").first()
        user_sub.ordered += 1
        user_sub.save()

        return instance
