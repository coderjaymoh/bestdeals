from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Flashsale model
class Flashsale(BaseModel):
    product_descriptions = models.CharField(max_length=200)
    products_left = models.CharField(max_length=100, null=True, blank=True)
    product_price = models.CharField(max_length=100)
    cash_saved = models.CharField(max_length=100)
    fetched_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_descriptions

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    is_registered = models.BooleanField(default=False)
    is_loggedin = models.BooleanField(default=False)

    def __str__(self):
        return self.client_name

class TrackedProduct(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, name='client')
    tracked_product_name = models.CharField(max_length=200)

    def __str__(self):
        return self.tracked_product_name


        # [{"model": "bestdeals.trackedproduct", "pk": 15, "fields": ''{"tracked_product_name": "watch"}}]