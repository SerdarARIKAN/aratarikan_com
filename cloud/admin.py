from django.contrib import admin
from cloud.models import File


class CloudAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Slayt Objesi', {
            'fields': (('file', 'published'),)
        }),
        ('Arkaplan', {
            'fields': (('description', 'date'),)
        })
    )

    list_display = ('pk', 'file', 'published', 'description', 'date')


admin.site.register(File, CloudAdmin)