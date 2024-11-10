from django.db import models
from django.conf import settings
from product.models import ProductModel
from datetime import datetime


class CartModel(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    when_added = models.DateTimeField(default=datetime.utcnow())
    is_ready_to_order = models.BooleanField(default=False)

    class Meta:
        ordering = ["-when_added"]
