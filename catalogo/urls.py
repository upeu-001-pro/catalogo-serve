from django.conf.urls import url, include
from rest_framework import routers

from .views.categoria_view import CategoriaViewSet
from .views.autor_view import AutorViewSet
from .views.libro_view import LibroViewSet

router = routers.DefaultRouter()

router.register(r'categorias', CategoriaViewSet)
router.register(r'autors', AutorViewSet, 'autors-view')
router.register(r'libros', LibroViewSet, 'libros-view')

urlpatterns = [

    url(r'^', include(router.urls)),

]
