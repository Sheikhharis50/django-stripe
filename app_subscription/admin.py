from django.contrib import admin

from app_subscription.models import (
    Subscription,
    UserSubscription,
)
from app_subscription.forms import UserSubscriptionForm


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "can_order",
    )


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    form = UserSubscriptionForm
    list_display = (
        "id",
        "user",
        "subscription",
        "ordered",
    )
