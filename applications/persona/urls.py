from django.contrib import admin
from django.urls import path
from . import views

#Varialbe desde django 2
app_name = "persona_app"

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(), 
        name='inicio'
    ),
    path(
        'lista-all-empleados/',
        views.ListAllEmpleados.as_view(),
        name='all_empleados'
    ),    
    path(
        'lista-by-area/<shorname>/', 
        views.ListByAreaEmpleado.as_view(),
        name='empleado_by_area'
    ),    
    path(
        'lista-emp-admin/', 
        views.ListEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),
    path('buscar-empleado/', views.ListempleadosByKword.as_view()),
    path('listar-empleado-habilidades/', views.ListHabilidadesEmpleados.as_view()),
    path(
        'ver-empleado/<pk>', 
        views.EmpleadoDetailView.as_view(),
        name='detail_empleado'
    ), 
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name = 'add_emeplado'
    ), 
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name='correcto'
    ),
    path(
        'update-empleado/<pk>', 
        views.EmpleadoUpdateView.as_view(), 
        name='modifica_empleado'
    ),
    path(
        'delete-empleado/<pk>', 
        views.EmpleadoDeleteView.as_view(), 
        name='elimina_empleado'
    ),
]