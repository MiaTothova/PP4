from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm


def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('home')
            messages.success(request,
                             'Your Booking has been succesful!')
    else:
        form = BookingForm()
    return render(request, 'booking/create.html', {'form': form})


class Index(TemplateView):
    template_name = 'booking/index.html'


class Menu(TemplateView):
    template_name = 'booking/menu.html'


class Create(TemplateView):
    template_name = 'booking/create.html'