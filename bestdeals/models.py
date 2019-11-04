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