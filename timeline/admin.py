from django.contrib import admin
from timeline.models import Point


class TimeLineAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Slayt Objesi', {
            'fields': (('slide_object_type', 'group', 'display_date', 'published'),)
        }),
        ('Başlangıç zamanı', {
            'fields': (('start_date', 'start_display_date'),)
        }),
        ('Bitiş zamanı', {
            'fields': (('end_date', 'end_display_date'),)
        }),
        ('Yazı', {
            'fields': (('text_headline', 'autolink'), ('text_text'))
        }),
        ('Medya', {
            'fields': (
                ('media_url', 'media_caption'), ('media_thumbnail',
                                                 'media_title'), ('media_alt', 'media_credit'),
                ('media_link_target', 'media_link'))
        }),
        ('Arkaplan', {
            'fields': (('background_url', 'background_color'),)
        })
    )

    list_display = ('text_headline', 'slide_object_type',
                    'start_date', 'end_date', 'group', 'published')


admin.site.register(Point, TimeLineAdmin)
