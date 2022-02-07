from django import forms
from django.db import models
from django.core import exceptions

from app_core.forms import ModelForm
from app_subscription.models import UserSubscription

from utils.enums import PaymentStatus


class UserSubscriptionForm(ModelForm):
    transaction_data = forms.JSONField(required=False)
    payment_status = forms.ChoiceField(required=False, choices=PaymentStatus.choices)

    class Meta:
        model = UserSubscription
        fields = ["subscription", "user", "transaction_data", "payment_status"]

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
