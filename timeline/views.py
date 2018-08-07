from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from timeline.models import Point
from timeline.serializers import TimeLineSerializer


class timeline_view(TemplateView):
    template_name = 'timeline/timeline.html'

class timeline_api_view(APIView):
    def get(self, request, format=None):
        point = Point.objects.filter(published=True)
        serializer = TimeLineSerializer(point, many=True)
        return Response(serializer.data)