from private_storage.views import PrivateStorageDetailView
from cloud.models import File
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


class cloud_list_view(ListView):
    model = File
    template_name = "cloud/cloud.html"
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            return File.objects.all()
        else:
            return File.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(cloud_list_view, self).get_context_data(**kwargs)

        if self.request.user.is_superuser:
            Files = File.objects.all()
        else:
            Files = File.objects.filter(published=True)

        paginator = Paginator(Files, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['list_exams'] = file_exams
        return context


class cloud_file_view(PrivateStorageDetailView):
    model = File
    model_file_field = 'file'

    def get_queryset(self, *args, **kwargs):
        return super(cloud_file_view, self).get_queryset(*args, **kwargs)

    def can_access_file(self, private_file):
        self.object = self.get_object()
        return self.request.user.is_superuser or self.object.published
