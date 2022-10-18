
from django.urls import path
from .views import (home, Contacto, About, ProyectoIntegrador, CrearFormato, EliminarFormato, EditarFormato, ListarFormato ,MostrarFormato,
CrearAlbum, EliminarAlbum ,EditarAlbum , ListarAlbum, MostrarAlbum, CrearTema, EliminarTema, EditarTema, ListarTema, MostrarTema, 
CrearInterprete, EliminarInterprete, EditarInterprete, ListarInterprete, CrearGenero, MostrarInterprete, EliminarGenero, EditarGenero, MostrarGenero ,ListarGenero,
CrearDiscografica,  EliminarDiscografica, EditarDiscografica, ListarDiscografica,  MostrarDiscografica )

urlpatterns = [

   
    path('',home, name="index"),  
    path('contacto/', Contacto.as_view(), name="contacto"),
    path('about/', About.as_view(), name="about"),
    
    path('proyecto',ProyectoIntegrador.as_view(), name="proyecto"),         
   
    path('crear-album' , CrearAlbum.as_view(), name='crear_album'),
    path('eliminar-album/<int:pk>' , EliminarAlbum.as_view(), name='eliminar_album'),
    path('editar-album/<int:pk>' , EditarAlbum.as_view(), name='editar_album'),
    path('listar-album' , ListarAlbum.as_view(), name='listar_album'),
    path('mostrar-album/<int:pk>/' , MostrarAlbum.as_view(), name='mostrar_album'),

    path('crear-tema' , CrearTema.as_view(), name='crear_tema'),
    path('eliminar-tema/<int:pk>' , EliminarTema.as_view(), name='eliminar_tema'),
    path('editar-tema/<int:pk>' , EditarTema.as_view(), name='editar_tema'),
    path('listar-tema' , ListarTema.as_view(), name='listar_tema'),
    path('mostrar-tema/<int:pk>/' , MostrarTema.as_view(), name='mostrar_tema'),

        #NOTA: respetar los nombres de las creacion de las funciones, si los mismos deciden cambiarlos deben a su vez, 
               #cambiar el nombre en cada modulo del ruteo que corresponda!!!

    path('crear-formato' , CrearFormato.as_view(), name='crear_formato'),
    path('eliminar-formato/<int:pk>' , EliminarFormato.as_view(), name='eliminar_formato'),
    path('editar-formato/<int:pk>' , EditarFormato.as_view(), name='editar_formato'),
    path('listar-formato' , ListarFormato.as_view(), name='listar_formato'),
    path('mostrar-formato/<int:pk>/' , MostrarFormato.as_view(), name='mostrar_formato'),

    path('crear-interprete' , CrearInterprete.as_view(), name='crear_interprete'),
    path('eliminar-interprete/<int:pk>' , EliminarInterprete.as_view(), name='eliminar_interprete'),
    path('editar-interprete/<int:pk>' , EditarInterprete.as_view(), name='editar_interprete'),
    path('listar-interprete' , ListarInterprete.as_view(), name='listar_interprete'),
    path('mostrar-interprete/<int:pk>/' , MostrarInterprete.as_view(), name='mostrar_interprete'),

    # los path de genero a completar por lizbeth

    # los path de discografica a completar por joaquin

]

