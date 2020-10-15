from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Flashsale models


class User(BaseModel):
    user_phone = models.IntegerField()

    def __str__(self):
        return str(self.user_phone)


class UserProduct(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    tracked_product = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user.user_phone)


class ScrapedProduct(BaseModel):
    product_descriptions = models.CharField(max_length=200)
    products_left = models.CharField(max_length=100, null=True, blank=True)
    product_price = models.CharField(max_length=100)
    cash_saved = models.CharField(max_length=100)
    fetched_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_descriptions

class TrackedProduct(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='user')
    tracked_product_name = models.CharField(max_length=200)

    def __str__(self):
        return self.tracked_product_name