from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class PaymentStatus(TextChoices):
    PENDING = "pending", _("Pending")
    PAID = "paid", _("Paid")
