from django.urls import path, include
from cloud.views import cloud_list_view
from cloud.views import cloud_file_view
import private_storage.urls


urlpatterns = [
    path('', cloud_list_view.as_view(), name="cloud"),
    path('<int:pk>/', cloud_file_view.as_view(), name="cloud_file")
]

urlpatterns += [
   path('private-media/', include(private_storage.urls)),
]