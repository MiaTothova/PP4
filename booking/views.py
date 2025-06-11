from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking


@login_required
def book_table(request):
    """
    Handle booking form submission and rendering.
    If the request is POST, validate and save the booking form.
    If the method is GET, renders a blank booking form.
    """
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your Booking has been successful!')
            return redirect('view_bookings')
    else:
        form = BookingForm()
    return render(request, 'booking/create.html', {'form': form})


class Index(TemplateView):
    """
    Render the home page (index.html).
    """
    template_name = 'booking/index.html'


class Menu(TemplateView):
    """
    Render the menu page (menu.html).
    """
    template_name = 'booking/menu.html'


class Create(TemplateView):
    """
    Render the booking creation page.
    """
    template_name = 'booking/create.html'


@login_required
def view_bookings(request):
    """
    Display all bookings made by the logged-in user.
    """
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    return render(request, 'booking/view_booking.html', {'bookings': bookings})


@login_required
def edit_booking(request, booking_id):
    """
    Edit an existing booking for the logged-in user.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been updated!')
            return redirect('view_bookings')
    else:
        form = BookingForm(instance=booking)

    return render(
        request,
        'booking/edit_booking.html',
        {
            'form': form,
            'booking': booking
        }
    )


@login_required
def delete_booking(request, booking_id):
    """
    Delete a booking for the logged-in user.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Your booking has been cancelled.')
        return redirect('view_bookings')

    return render(request, 'booking/delete_booking.html', {'booking': booking})
