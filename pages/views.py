from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        kwargs['page_title'] = 'Home'
        return kwargs
