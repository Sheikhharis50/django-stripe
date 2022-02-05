from django.contrib import admin

from app_order.models import Order
from app_order.forms import OrderForm


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    list_display = (
        "id",
        "user",
        "ordered_at",
    )
