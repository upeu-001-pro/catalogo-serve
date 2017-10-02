from uuid import uuid4
from django.db import models
from .libro import Libro


class Ejemplar(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    codigo = models.CharField(max_length=50)
    libro = models.ForeignKey(  # related_name='ejemplar_set',
        Libro)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ejemplar"
        verbose_name_plural = "Ejemplares"
        permissions = (
            ('list_ejemplar', 'Can list ejemplar'),
            ('get_ejemplar', 'Can get ejemplar'),
        )

    def __str__(self):
        return '%s %s' % (self.codigo, self.libro.nombre)
