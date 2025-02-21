from django.urls import path
from .views import Index, Menu


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('menu/', Menu.as_view(), name='menu'),
]