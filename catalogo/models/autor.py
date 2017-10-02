from uuid import uuid4
from django.db import models


class Autor(models.Model):
    """
    docs
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    direccion = models.TextField(null=True, blank=True)
    fecha_nac = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        docs
        """
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        permissions = (
            ('list_autor', 'Can list autor'),
            ('get_autor', 'Can get autor'),
        )

    def __str__(self):
        return self.nombre
