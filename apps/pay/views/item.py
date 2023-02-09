import stripe
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from apps.pay.models import Item
from core import settings
from core.settings import ENV

stripe.api_key = ENV.get("STRIPE_KEY")


class CreateCheckoutSessionView(APIView):
    """Создаем сессию  и передаем ее ID"""

    def post(self, request, *args, **kwargs):
        product = Item.objects.get(id=kwargs["pk"])
        YOUR_DOMAIN = "http://localhost:8003"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                            'description': product.description,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/apps/pay/success/',
            cancel_url=YOUR_DOMAIN + '/apps/pay/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class GetProductPageView(APIView):
    """Показ информации о продукте"""
    model = Item
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product.html'

    def get(self, request, **kwargs):
        product = Item.objects.get(id=kwargs["pk"])
        context = {
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        }
        return render(request=request, template_name="product.html", context=context)
