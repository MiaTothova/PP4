from django.urls import path
from .views import Index, Menu, Create


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('menu/', Menu.as_view(), name='menu'),
    path('create/', Create.as_view(), name='create'),

]