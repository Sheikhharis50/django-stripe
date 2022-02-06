from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # custom
    path("", include("app_core.urls")),
    path("subscription/", include("app_subscription.urls")),
    # default
    path("admin/", admin.site.urls),
]
