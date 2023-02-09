from django.urls import path

from pay.views.item import GetProductPageView, CancelView, SuccessView, CreateCheckoutSessionView
from pay.views.webhook import stripe_webhook

urlpatterns = [
    path("item/<pk>/", GetProductPageView.as_view()),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('buy/<pk>', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
