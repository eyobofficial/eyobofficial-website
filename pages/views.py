from django.views.generic import TemplateView

from .mixins import HomePage


class HomeView(HomePage, TemplateView):
    template_name = 'pages/home.html'
