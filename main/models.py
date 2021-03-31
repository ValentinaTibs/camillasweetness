from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Pagina(models.Model):
    nome        = models.CharField(max_length=200)
    contenuto   = HTMLField()
    slug        = models.CharField(max_length=200, unique=True, blank=True,null=False)

    class Meta: 
        verbose_name = "Pagina"
        verbose_name_plural = "Pagine"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.nome.replace(" ","-").lower()

        super().save(*args, **kwargs)  # Call the "real" save() method.
