from uuid import uuid4
from django.db import models
from .categoria import Categoria
from .autor import Autor
from ..enums import LIBRO_TIPO_CHOICES, FISICO


class Libro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, null=True, blank=True)
    autors = models.ManyToManyField(Autor, blank=True)
    tipo = models.CharField(
        max_length=50, choices=LIBRO_TIPO_CHOICES, default=FISICO)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        permissions = (
            ('list_libro', 'Can list libro'),
            ('get_libro', 'Can get libro'),
        )

    def __str__(self):
        return self.nombre
