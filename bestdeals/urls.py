from django.urls import path
from bestdeals import views

urlpatterns = [
    path('', views.home, name='home'),
]