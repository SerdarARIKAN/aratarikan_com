from rest_framework import serializers
from timeline.models import Point


class TimeLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = (
            'unique_id',
            'slide_object_type',
            'group',
            'display_date',
            'published',
            'start_date',
            'start_display_date',
            'end_date',
            'end_display_date',
            'text_headline',
            'autolink',
            'text_text',
            'media_url',
            'media_caption',
            'media_thumbnail',
            'media_title',
            'media_alt',
            'media_credit',
            'media_link_target',
            'media_link',
            'background_url',
            'background_color')
