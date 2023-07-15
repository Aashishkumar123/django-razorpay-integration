from django.urls import path
from .import views


urlpatterns = [
    path("", views.subscription, name="subscription"),
    path("create/order/", views.create_order_view, name="create-order"),
    path("verify/payment/", views.verify_payment, name="verify-payment"),
    path("success/payment/", views.payment_success, name="success-payment"),
    path("failed/payment/", views.payment_failed, name="failed-payment"),
]
