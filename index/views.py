from django.views.generic import TemplateView


class index_view(TemplateView):
    template_name = 'index/index.html'
