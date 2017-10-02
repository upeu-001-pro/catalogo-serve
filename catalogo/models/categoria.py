from uuid import uuid4

from django.db import models


# Create your models here.


class Categoria(models.Model):
    """
    docs
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    nombre = models.CharField(max_length=60)

    codigo = models.CharField(max_length=15, null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        """
        docs
        """
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        permissions = (
            ('list_categoria', 'Can list categoria'),
            ('get_categoria', 'Can get categoria'),
        )

    def __str__(self):
        return self.nombre
