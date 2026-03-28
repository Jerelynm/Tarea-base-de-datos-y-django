from django.shortcuts import render, redirect, get_object_or_404
from universidad.Models.Alumno.models import Alumno
from .models import Curso, Catedratico, AsignacionCurso, InscripcionAlumno, Calificacion
from .forms import (
    CursoForm,
    CatedraticoForm,
    AsignacionCursoForm,
    InscripcionAlumnoForm,
    CalificacionForm
)


def dashboard(request):
    context = {
        'total_alumnos': Alumno.objects.count(),
        'activos': Alumno.objects.filter(is_active=True).count(),
        'inactivos': Alumno.objects.filter(is_active=False).count(),
        'total_cursos': Curso.objects.count(),
        'total_catedraticos': Catedratico.objects.count(),
        'total_asignaciones': AsignacionCurso.objects.count(),
        'total_inscripciones': InscripcionAlumno.objects.count(),
        'total_calificaciones': Calificacion.objects.count(),
    }
    return render(request, 'core/dashboard.html', context)


# ---------------- CURSO ----------------
def cursos(request):
    datos = Curso.objects.all()
    return render(request, 'curso/list.html', {'datos': datos})


def curso_create(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cursos')
    return render(request, 'curso/form.html', {'form': form, 'titulo': 'Nuevo curso'})


def curso_update(request, pk):
    item = get_object_or_404(Curso, pk=pk)
    form = CursoForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('cursos')
    return render(request, 'curso/form.html', {'form': form, 'titulo': 'Editar curso'})


def curso_delete(request, pk):
    item = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('cursos')
    return render(request, 'curso/delete.html', {'item': item, 'titulo': 'Eliminar curso'})


# ---------------- CATEDRATICO ----------------
def catedraticos(request):
    datos = Catedratico.objects.all()
    return render(request, 'catedraticos/list.html', {'datos': datos})


def catedratico_create(request):
    form = CatedraticoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catedraticos')
    return render(request, 'catedraticos/form.html', {'form': form, 'titulo': 'Nuevo catedrático'})


def catedratico_update(request, pk):
    item = get_object_or_404(Catedratico, pk=pk)
    form = CatedraticoForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('catedraticos')
    return render(request, 'catedraticos/form.html', {'form': form, 'titulo': 'Editar catedrático'})


def catedratico_delete(request, pk):
    item = get_object_or_404(Catedratico, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('catedraticos')
    return render(request, 'catedraticos/delete.html', {'item': item, 'titulo': 'Eliminar catedrático'})


# ---------------- ASIGNACION CURSO ----------------
def asignacion_curso(request):
    datos = AsignacionCurso.objects.select_related('curso', 'catedratico').all()
    return render(request, 'asignacion_curso/list.html', {'datos': datos})


def asignacion_create(request):
    form = AsignacionCursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('asignacion_curso')
    return render(request, 'asignacion_curso/form.html', {'form': form, 'titulo': 'Nueva asignación'})


def asignacion_update(request, pk):
    item = get_object_or_404(AsignacionCurso, pk=pk)
    form = AsignacionCursoForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('asignacion_curso')
    return render(request, 'asignacion_curso/form.html', {'form': form, 'titulo': 'Editar asignación'})


def asignacion_delete(request, pk):
    item = get_object_or_404(AsignacionCurso, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('asignacion_curso')
    return render(request, 'asignacion_curso/delete.html', {'item': item, 'titulo': 'Eliminar asignación'})


# ---------------- INSCRIPCION ALUMNO ----------------
def inscripcion_alumno(request):
    datos = InscripcionAlumno.objects.select_related('alumno', 'curso').all()
    return render(request, 'inscripcion_alumno/list.html', {'datos': datos})


def inscripcion_create(request):
    form = InscripcionAlumnoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inscripcion_alumno')
    return render(request, 'inscripcion_alumno/form.html', {'form': form, 'titulo': 'Nueva inscripción'})


def inscripcion_update(request, pk):
    item = get_object_or_404(InscripcionAlumno, pk=pk)
    form = InscripcionAlumnoForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('inscripcion_alumno')
    return render(request, 'inscripcion_alumno/form.html', {'form': form, 'titulo': 'Editar inscripción'})


def inscripcion_delete(request, pk):
    item = get_object_or_404(InscripcionAlumno, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('inscripcion_alumno')
    return render(request, 'inscripcion_alumno/delete.html', {'item': item, 'titulo': 'Eliminar inscripción'})


# ---------------- CALIFICACIONES ----------------
def calificaciones(request):
    datos = Calificacion.objects.select_related('inscripcion').all()
    return render(request, 'calificaciones/list.html', {'datos': datos})


def calificacion_create(request):
    form = CalificacionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('calificaciones')
    return render(request, 'calificaciones/form.html', {'form': form, 'titulo': 'Nueva calificación'})


def calificacion_update(request, pk):
    item = get_object_or_404(Calificacion, pk=pk)
    form = CalificacionForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('calificaciones')
    return render(request, 'calificaciones/form.html', {'form': form, 'titulo': 'Editar calificación'})


def calificacion_delete(request, pk):
    item = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('calificaciones')
    return render(request, 'calificaciones/delete.html', {'item': item, 'titulo': 'Eliminar calificación'})

# ---------------- REPORTES ----------------
def reporte_inscripciones(request):
    datos = InscripcionAlumno.objects.select_related('alumno', 'curso').all()
    return render(request, 'reportes/reporte_inscripciones.html', {'datos': datos})


def reporte_asignaciones(request):
    datos = AsignacionCurso.objects.select_related('curso', 'catedratico').all()
    return render(request, 'reportes/reporte_asignaciones.html', {'datos': datos})
