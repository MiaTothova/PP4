from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'booking/index.html'


class Menu(TemplateView):
    template_name = 'booking/menu.html'