from django.urls import path

from app_subscription.views import (
    SubscriptionView,
    SuccessView,
    CancelView,
)

urlpatterns = [
    path("<int:pk>", SubscriptionView.as_view(), name="subscription-view"),
    path("<int:pk>/success", SuccessView.as_view(), name="success-view"),
    path("<int:pk>/cancel", CancelView.as_view(), name="cancel-view"),
]
