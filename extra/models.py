from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

class Carusel(models.Model):
    title = models.CharField("Nomi", max_length=200)
    image = models.ImageField("Rasm", upload_to='carusel/')

    class Meta:
        verbose_name = 'Carusel'
        verbose_name_plural = 'Carusel'

    def __str__(self):
        return self.title    



