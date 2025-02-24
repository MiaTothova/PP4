from django.urls import path
from .views import Index, Menu, Create, book_table


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('menu/', Menu.as_view(), name='menu'),
    path('create/', book_table, name='create'),

]