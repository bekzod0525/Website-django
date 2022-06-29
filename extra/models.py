from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from tabnanny import verbose
from unicodedata import category

class Carusel(models.Model):
    title = models.CharField("Nomi", max_length=200)
    image = models.ImageField("Rasm", upload_to='carusel/')

    class Meta:
        verbose_name = 'Carusel'
        verbose_name_plural = 'Carusel'

    def __str__(self):
        return self.title    



class ImgCategory(models.Model):
    name = models.CharField("Kategoriya", max_length=255)

    class Meta:
        verbose_name = "kategoriya"
        verbose_name_plural = "Rasm kategoriyalari"

    def __str__(self) -> str:
        return self.name


class Gallery(models.Model):
    category = models.ForeignKey(
        ImgCategory,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    title = models.CharField("nomi", max_length=255, blank=True)
    image = models.ImageField("rasm", upload_to="images/")

    class Meta:
        ordering = ('id',)
        verbose_name = "rasm"
        verbose_name_plural = "Rasmlar"

    def __str__(self) -> str:
        return f"{self.id} - rasm"

