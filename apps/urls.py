from django.urls import path, include

urlpatterns = [
    path('pay/', include("pay.urls")),
    # path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),

]
