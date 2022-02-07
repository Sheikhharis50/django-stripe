from django.views.generic import TemplateView
from http import HTTPStatus

from app_core.response import Response
from app_subscription.models import Subscription
from app_subscription.forms import UserSubscriptionForm


class SubscriptionView(TemplateView):
    template_name = "pages/subscription.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subscription"] = Subscription.objects.filter(id=pk).first()
        return context

    def get(self, request, pk, **kwargs):
        form = UserSubscriptionForm(
            data=dict(
                subscription=pk,
                user=request.user.id,
            )
        )
        if form.is_valid():
            context = self.get_context_data(pk, **kwargs)
            return self.render_to_response(context)
        return Response(status=HTTPStatus.FORBIDDEN)


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
