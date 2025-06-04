from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking


def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your Booking has been successful!')
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'booking/create.html', {'form': form})


class Index(TemplateView):
    template_name = 'booking/index.html'


class Menu(TemplateView):
    template_name = 'booking/menu.html'


class Create(TemplateView):
    template_name = 'booking/create.html'


@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    return render(request, 'booking/view_booking.html', {'bookings': bookings})