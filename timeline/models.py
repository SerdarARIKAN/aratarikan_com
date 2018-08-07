from django.db import models
import uuid


class Point(models.Model):
    unique_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    slide_object_type_choices = (
        ('event', 'Olay'),
        ('title', 'Başlık'),
        ('era', 'Dönem')
    )

    slide_object_type = models.CharField(
        choices=slide_object_type_choices,
        default="event",
        max_length=8,
        verbose_name="Obje Tipi",
        help_text="Genellikle olay girişi olur.")

    group = models.CharField(
        blank=True,
        null=True,
        verbose_name="Obje grubu",
        help_text="Aynı grupta yer alan objeler aynı satırda gösterilir.",
        max_length=32)
    display_date = models.CharField(
        blank=True,
        null=True,
        verbose_name="Görünüm zamanı",
        help_text="Zamanının görünüm tercihi.",
        max_length=32)

    published = models.BooleanField(
        verbose_name="Yayınlandı",
        help_text="Objenin yayınlanmasını istemiyorsanız işartlemeyin.")

    start_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Başlangıç zamanı",
        help_text="Zaman çizelgesinde obje başlangıç konumu.")
    start_display_date = models.CharField(
        blank=True,
        null=True,
        verbose_name="Başlangıç görünüm zamanı",
        help_text="Başlangıç zamanının görünüm tercihi.",
        max_length=32)

    end_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Bitiş zamanı",
        help_text="Zaman çizelgesinde obje bitiş konumu.")
    end_display_date = models.CharField(
        blank=True,
        null=True,
        verbose_name="Bitiş görünüm zamanı",
        help_text="Bitiş zamanının görünüm tercihi.",
        max_length=32)

    text_headline = models.CharField(
        blank=True,
        null=True,
        verbose_name="Başlık",
        help_text="Maksimum 128 karakterlik bir başlık.",
        max_length=128)
    autolink = models.BooleanField(
        verbose_name="Metin içinde link var mı?",
        help_text="Linklerin aktif edilmesi için işaretleyiniz.")
    text_text = models.TextField(
        blank=True,
        null=True,
        verbose_name="Metin",
        help_text="Sınırlama yok.")

    media_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Medya linki",
        help_text="Resim, Video, Ses, Harita linki.")
    media_caption = models.CharField(
        blank=True,
        null=True,
        verbose_name="Medya yazısı",
        help_text="Medyada görünecek yazı.",
        max_length=32)
    media_thumbnail = models.URLField(
        blank=True,
        null=True,
        verbose_name="Medya öngörünüm linki",
        help_text="Küçük resim linki.")
    media_title = models.CharField(
        blank=True,
        null=True,
        verbose_name="Medya başlığı",
        help_text="Medyada görünecek başlık.",
        max_length=128)
    media_alt = models.URLField(
        blank=True,
        null=True,
        verbose_name="Medya hata resmi",
        help_text="Medya yüklemediğinde yüklenecek alternatif link.")
    media_credit = models.CharField(
        blank=True,
        null=True,
        verbose_name="Medya telifi",
        help_text="Varsa telifin ait olduğu kişi/kuruluş.",
        max_length=32)
    media_link_target = models.URLField(
        blank=True,
        null=True,
        verbose_name="Medya hedefi",
        help_text="Medyaya tıklandığında nereye gidilecek.")
    media_link = models.CharField(
        blank=True,
        null=True,
        verbose_name="Medya hedef başlığı",
        help_text="Tıklanabilir link başlığı.",
        max_length=32)

    background_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Arkaplan linki",
        help_text="Herhangi bir resim linki.")
    background_color = models.CharField(
        blank=True,
        null=True,
        verbose_name="Arkaplan rengi",
        help_text="Herhangi bir rengin hex kodu.",
        max_length=8)
