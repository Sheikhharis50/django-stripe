from django.urls import path

from app_core.views import (
    LandingView,
    CreateCheckoutSessionView,
    StripeWebhookView,
)

urlpatterns = [
    path("", LandingView.as_view(), name="landing-view"),
    path(
        "create-checkout-session/<int:subscription_id>/",
        CreateCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path("webhooks/stripe/", StripeWebhookView.as_view(), name="stripe-webhook"),
]
