from django.db import models
from django.conf import settings
from cart.models import CartModel
from datetime import datetime


class Status(models.TextChoices):

    GETREADY = "GET READY"
    DELIVERED = "DELIVERED"
    READY = "READY"
    PAYED = "PAYED"


class OrderModel(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ManyToManyField(CartModel)
    when_created_at = models.DateTimeField(default=datetime.utcnow())
    status = models.CharField(choices=Status, default=Status.GETREADY, max_length=45)

    class Meta:
        ordering = ["-when_created_at"]

 
