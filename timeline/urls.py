from django.urls import path
from timeline.views import timeline_view
from timeline.views import timeline_api_view

urlpatterns = [
    path('', timeline_view.as_view(), name='timeline'),
    path('api/', timeline_api_view.as_view(), name='timeline_api'),
]