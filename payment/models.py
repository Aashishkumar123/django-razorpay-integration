from django.db import models

class Transaction(models.Model):
    amount = models.IntegerField(verbose_name="Amount")
    order_id = models.CharField(max_length=100, verbose_name="Order ID")
    payment_id = models.CharField(max_length=100, verbose_name="Payment ID")
    signature = models.CharField(max_length=100, verbose_name="Signature")

    def __str__(self):
        return str(self.order_id)
