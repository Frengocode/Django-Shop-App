from django.db import models
from datetime import datetime
from django.conf import settings


class ProductCategory(models.TextChoices):
    TECHNIQUE = "TECHNIQUE"
    MEAL = "MEAL"
    CLOTHES = "CLOTHES"
    BOOK = "BOOK"
    HOUSE = "HOUSE"
    CAR = "CAR"
    BUISNES = "BUISNES"
    OTHER = "OTHER"


class ProductModel(models.Model):

    product_title = models.CharField(max_length=30, null=False)
    product_picture = models.ImageField(upload_to="product-picture/", null=False)
    description = models.CharField(max_length=250, null=True)
    price = models.BigIntegerField()
    product_category = models.CharField(
        choices=ProductCategory, default=None, max_length=50, null=False
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_discount = models.BooleanField(default=False)
    date_of_pub = models.DateTimeField(default=datetime.utcnow())

    def __str__(self):
        return f"Title - {self.product_title}, Price {self.price}, When Created {self.date_of_pub}"

    class Meta:
        ordering = ["-date_of_pub"]
