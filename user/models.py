from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import ProductModel


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="user-pictures/", null=True)
    phone_number = models.BigIntegerField(null=True)
    products = models.ManyToManyField(ProductModel, verbose_name="user_products")
