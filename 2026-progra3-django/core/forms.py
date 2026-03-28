from django import forms
from .models import Curso, Catedratico, AsignacionCurso, InscripcionAlumno, Calificacion


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


class CatedraticoForm(forms.ModelForm):
    class Meta:
        model = Catedratico
        fields = '__all__'


class AsignacionCursoForm(forms.ModelForm):
    class Meta:
        model = AsignacionCurso
        fields = '__all__'


class InscripcionAlumnoForm(forms.ModelForm):
    class Meta:
        model = InscripcionAlumno
        fields = '__all__'
        widgets = {
            'fecha_inscripcion': forms.DateInput(attrs={'type': 'date'})
        }


class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = '__all__'


