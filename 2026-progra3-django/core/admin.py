from django.contrib import admin
from .models import Curso, Catedratico, AsignacionCurso, InscripcionAlumno, Calificacion

admin.site.register(Curso)
admin.site.register(Catedratico)
admin.site.register(AsignacionCurso)
admin.site.register(InscripcionAlumno)
admin.site.register(Calificacion)
