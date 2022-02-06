from django.db import models
from django.conf import settings


class Subscription(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    can_order = models.IntegerField(default=10)
    price = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.name)


class UserSubscription(models.Model):
    subscription = models.ForeignKey(
        to="app_subscription.Subscription",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    ordered = models.IntegerField(default=0)

    def __str__(self):
        return "{} has subscribed with {}".format(
            self.user.get_full_name(),
            self.subscription.name,
        )
