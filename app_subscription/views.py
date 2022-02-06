from django.views.generic import TemplateView

from app_subscription.models import Subscription


class SubscriptionView(TemplateView):
    template_name = "pages/subscription.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subscription"] = Subscription.objects.filter(id=pk).first()
        return context


class SuccessView(TemplateView):
    template_name = "pages/success.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subscription"] = Subscription.objects.filter(id=pk).first()
        return context


class CancelView(TemplateView):
    template_name = "pages/cancel.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subscription"] = Subscription.objects.filter(id=pk).first()
        return context
