from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .razorpay.main import RazorpayClient
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction
from django.conf import settings


rzClient = RazorpayClient()


def subscription(request):
    context = {"RAZORPAY_KEY_ID": settings.RAZORPAY_KEY_ID}
    return render(request, "subscription.html", context=context)


def create_order_view(request):
    if request.method == "POST":
        amount = int(request.POST.get("amount"))
        currency = request.POST.get("currency")
        create_order = rzClient.create_order(amount=amount, currency=currency)
        response = {
            "status_code": "200",
            "message": "ok",
            "data": create_order
        }
        return JsonResponse(response)

@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        order_id = request.POST.get("razorpay_order_id")
        payment_id = request.POST.get("razorpay_payment_id")
        razorpay_signature = request.POST.get("razorpay_signature")
        amount = request.GET.get("amount")
        if rzClient.verify_payment_signature(
            razorpay_order_id = order_id,
            razorpay_payment_id = payment_id,
            razorpay_signature = razorpay_signature
        ):
            Transaction.objects.get_or_create(
                order_id = order_id,
                payment_id = payment_id,
                signature = razorpay_signature,
                amount = amount
            )
            return redirect("/success/payment/")
        else:
            return redirect("/failed/payment/")

def payment_success(request):
    return render(request, "payment_success.html")

def payment_failed(request):
    return render(request, "payment_failed.html")
