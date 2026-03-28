from django.urls import path
from . import views

app_name = 'alumno'

urlpatterns = [
    path('', views.alumno_list, name='list'),
    path('nuevo/', views.alumno_create, name='create'),
    path('<int:pk>/', views.alumno_detail, name='detail'),
    path('editar/<int:pk>/', views.alumno_edit, name='update'),
    path('eliminar/<int:pk>/', views.alumno_delete, name='delete'),
]