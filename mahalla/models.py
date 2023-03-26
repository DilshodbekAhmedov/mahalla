from django.db import models
from django.contrib.auth.models import User


class Sector(models.Model):
    name = models.CharField(verbose_name="Sektor nomi", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sektor"
        verbose_name_plural = "Sektrlar"
        ordering = "id",


class Neighborhood(models.Model):
    sector = models.ForeignKey('Sector', on_delete=models.PROTECT,
                               help_text="Mahalla qaysi sektorga tegishli ekanligini tanlang")
    name = models.CharField(verbose_name="Mahalla nomi", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahalla"
        verbose_name_plural = "Mahallalar"
        ordering = "id",


class Citizen(models.Model):
    GENDER = (
        ("male", "Erkak"),
        ('female', 'Ayol'),
    )
    EDUCATED = (
        ("middle", "O'rta ma'lumotli"),
        ("senior", "Oliy ma'lumotli")
    )
    IRAN_NOTEBOOK = (
        ("yes", "ha"),
        ("no", "yo'q"),
    )
    ABROAD = (
        ('yes', 'ha'),
        ("no", "yo'q"),
    )
    DISABILITY = (
        ('yes', 'ha'),
        ("no", "yo'q"),
    )
    WOMANS_NOTEBOOK = (
        ("yes", "ha"),
        ("no", "yo'q"),
    )
    PENSIONER = (
        ('yes', 'ha'),
        ('no', "yo'q")
    )
    neighborhood = models.ForeignKey('Neighborhood', verbose_name="Mahallani tanlang",
                                     on_delete=models.PROTECT)
    full_name = models.CharField(verbose_name='F.I.O.', max_length=255)
    passport = models.CharField(verbose_name='Pasport seriyasi', max_length=20)
    birthdate = models.DateField(verbose_name='Tug`ilgan sanasi')
    gender = models.CharField(
        max_length=255,
        choices=GENDER,
        verbose_name="Fuqoro jinsi",
    )
    educated = models.CharField(
        verbose_name="Fuqoro ma'lumoti",
        max_length=255,
        choices=EDUCATED,
    )
    address = models.TextField(verbose_name="Fuqoro manzili")

    iron_notebook = models.CharField(
        verbose_name="Temir daftarda bormi",
        max_length=255,
        choices=IRAN_NOTEBOOK,
    )

    abroad = models.CharField(
        verbose_name="Xozir chet eldami",
        max_length=255,
        choices=ABROAD,
    )

    disabiltiy = models.CharField(
        verbose_name="Nogironligi bormi",
        max_length=20,
        choices=DISABILITY,
    )

    womens_notebook = models.CharField(
        verbose_name="Ayollar daftarida bormi",
        max_length=20,
        choices=WOMANS_NOTEBOOK
    )
    pensioner = models.CharField(
        verbose_name="Pensiyoner",
        max_length=255,
        choices=PENSIONER,
        null=True
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Fuqaro"
        verbose_name_plural = "Fuqarolar"
        ordering = ("id",)
