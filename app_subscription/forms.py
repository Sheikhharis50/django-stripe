from django.db import models
from django.core import exceptions

from app_core.forms import ModelForm
from app_subscription.models import UserSubscription


class UserSubscriptionForm(ModelForm):
    class Meta:
        model = UserSubscription
        fields = ["subscription", "user"]

    def clean_user(self):
        user = self.cleaned_data.get("user")
        subscription = self.cleaned_data.get("subscription")
        if (
            UserSubscription.objects.select_related("subscription")
            .filter(user=user, ordered__lt=models.F("subscription__can_order"))
            .exists()
        ):
            raise exceptions.ValidationError(
                f"{user.get_full_name()} has already {subscription.name} subscription."
            )
        return user
