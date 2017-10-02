from django.contrib import admin
from .models.categoria import Categoria
from .models.autor import Autor
from .models.libro import Libro
from .models.ejemplar import Ejemplar

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):

    """docstring for CategoriaAdmin"""

    list_display = ("nombre", "codigo", "estado")
    search_fields = ("nombre", "codigo",)
    list_per_page = 3


class AutorAdmin(admin.ModelAdmin):

    """docstring for AutorAdmin"""

    list_display = ("nombre", "direccion", "fecha_nac")
    search_fields = ("nombre", "direccion",)
    list_per_page = 2


admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Autor, AutorAdmin)


class LibroAdmin(admin.ModelAdmin):

    list_display = ("nombre", "categoria", "created_at", "updated_at")


admin.site.register(Libro, LibroAdmin)
