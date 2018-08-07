from django.db import models
from private_storage.fields import PrivateFileField


class File(models.Model):
    file = PrivateFileField("File")
    published = models.BooleanField()

    description = models.CharField(
        blank=True,
        null=True,
        verbose_name="Açıklama",
        help_text="Varsa dosya ile ilgili açıklama.",
        max_length=64)
    date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Dosyanın ürtildiği tarih",
        help_text="Biliniyorsa.")
