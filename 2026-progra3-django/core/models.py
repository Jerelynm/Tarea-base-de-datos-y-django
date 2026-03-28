from django.db import models
from universidad.Models.Alumno.models import Alumno


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Catedratico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class AsignacionCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    catedratico = models.ForeignKey(Catedratico, on_delete=models.CASCADE)
    seccion = models.CharField(max_length=10)
    ciclo = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.curso} - {self.catedratico}"


class InscripcionAlumno(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
    estado = models.CharField(max_length=20, default='Activa')

    def __str__(self):
        return f"{self.alumno} - {self.curso}"


class Calificacion(models.Model):
    inscripcion = models.ForeignKey(InscripcionAlumno, on_delete=models.CASCADE)
    unidad = models.CharField(max_length=30)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    observacion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.inscripcion} - {self.nota}"