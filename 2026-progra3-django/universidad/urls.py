from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),

    path('alumnos/', include('universidad.Models.Alumno.urls')),

    path('cursos/', views.cursos, name='cursos'),
    path('cursos/nuevo/', views.curso_create, name='curso_create'),
    path('cursos/editar/<int:pk>/', views.curso_update, name='curso_update'),
    path('cursos/eliminar/<int:pk>/', views.curso_delete, name='curso_delete'),

    path('catedraticos/', views.catedraticos, name='catedraticos'),
    path('catedraticos/nuevo/', views.catedratico_create, name='catedratico_create'),
    path('catedraticos/editar/<int:pk>/', views.catedratico_update, name='catedratico_update'),
    path('catedraticos/eliminar/<int:pk>/', views.catedratico_delete, name='catedratico_delete'),

    path('asignacion-curso/', views.asignacion_curso, name='asignacion_curso'),
    path('asignacion-curso/nuevo/', views.asignacion_create, name='asignacion_create'),
    path('asignacion-curso/editar/<int:pk>/', views.asignacion_update, name='asignacion_update'),
    path('asignacion-curso/eliminar/<int:pk>/', views.asignacion_delete, name='asignacion_delete'),

    path('inscripcion-alumno/', views.inscripcion_alumno, name='inscripcion_alumno'),
    path('inscripcion-alumno/nuevo/', views.inscripcion_create, name='inscripcion_create'),
    path('inscripcion-alumno/editar/<int:pk>/', views.inscripcion_update, name='inscripcion_update'),
    path('inscripcion-alumno/eliminar/<int:pk>/', views.inscripcion_delete, name='inscripcion_delete'),

    path('calificaciones/', views.calificaciones, name='calificaciones'),
    path('calificaciones/nuevo/', views.calificacion_create, name='calificacion_create'),
    path('calificaciones/editar/<int:pk>/', views.calificacion_update, name='calificacion_update'),
    path('calificaciones/eliminar/<int:pk>/', views.calificacion_delete, name='calificacion_delete'),
]

