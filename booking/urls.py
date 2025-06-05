from django.urls import path
from .views import Index, Menu, Create, book_table
from . import views


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('menu/', Menu.as_view(), name='menu'),
    path('create/', book_table, name='create'),
    path('view_booking/', views.view_bookings, name='view_bookings'),
    path('edit-booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),

]
