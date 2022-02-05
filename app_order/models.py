from django.db import models
from django.conf import settings

from utils.helpers import readable_date


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    description = models.TextField(max_length=1000, default="Order description.")
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{} has ordered at {}".format(
            self.user.get_full_name(),
            readable_date(self.ordered_at),
        )
