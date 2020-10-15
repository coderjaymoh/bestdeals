from django.contrib import admin
from bestdeals.models import User, ScrapedProduct, UserProduct

admin.site.register(User)
admin.site.register(UserProduct)
admin.site.register(ScrapedProduct)