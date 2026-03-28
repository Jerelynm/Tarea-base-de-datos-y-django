import random
from datetime import date, timedelta
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction

from core.models import Curso, Catedratico, AsignacionCurso, InscripcionAlumno, Calificacion
from universidad.Models.Alumno.models import Alumno


class Command(BaseCommand):
    help = "Puebla la base de datos con 10,000 registros"

    def generar_nombre(self):
        nombres = [
            "Juan", "María", "Carlos", "Ana", "Luis", "Sofía", "Pedro", "Lucía",
            "Miguel", "Andrea", "José", "Valeria", "Pablo", "Camila", "Daniel",
            "Fernanda", "Ricardo", "Paola", "Jorge", "Gabriela"
        ]
        apellidos = [
            "Pérez", "López", "García", "Martínez", "Ramírez", "Torres",
            "Hernández", "Castillo", "Morales", "Gómez", "Flores", "Méndez"
        ]
        return random.choice(nombres), random.choice(apellidos)

    def generar_fecha_nacimiento(self):
        inicio = date(1995, 1, 1)
        fin = date(2008, 12, 31)
        dias = (fin - inicio).days
        return inicio + timedelta(days=random.randint(0, dias))

    def generar_fecha_inscripcion(self):
        inicio = date(2024, 1, 1)
        fin = date.today()
        dias = (fin - inicio).days
        return inicio + timedelta(days=random.randint(0, dias))

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Iniciando carga de datos..."))

        # Limpiar datos en orden correcto por dependencias
        Calificacion.objects.all().delete()
        InscripcionAlumno.objects.all().delete()
        AsignacionCurso.objects.all().delete()
        Catedratico.objects.all().delete()
        Curso.objects.all().delete()
        Alumno.objects.all().delete()

        # 1. Alumnos: 3000
        alumnos = []
        for i in range(3000):
            nombre, apellido = self.generar_nombre()
            alumnos.append(
                Alumno(
                    first_name=nombre,
                    last_name=apellido,
                    email=f"{nombre.lower()}{apellido.lower()}{i}@gmail.com",
                    phone=f"3000{i:04d}"[:20],
                    gender=random.choice(["M", "F"]),
                    birth_date=self.generar_fecha_nacimiento(),
                    is_active=random.choice([True, False]),
                )
            )
        Alumno.objects.bulk_create(alumnos)
        alumnos = list(Alumno.objects.all())
        self.stdout.write(self.style.SUCCESS("3000 alumnos creados"))

        # 2. Cursos: 100
        cursos = []
        for i in range(100):
            cursos.append(
                Curso(
                    nombre=f"Curso {i + 1}",
                    codigo=f"CUR-{i + 1:03d}",
                    creditos=random.randint(1, 5),
                )
            )
        Curso.objects.bulk_create(cursos)
        cursos = list(Curso.objects.all())
        self.stdout.write(self.style.SUCCESS("100 cursos creados"))

        # 3. Catedráticos: 100
        catedraticos = []
        for i in range(100):
            nombre, apellido = self.generar_nombre()
            catedraticos.append(
                Catedratico(
                    nombre=nombre,
                    apellido=apellido,
                    profesion=random.choice([
                        "Ingeniero en Sistemas",
                        "Licenciado en Matemática",
                        "Ingeniero Industrial",
                        "Licenciado en Educación",
                    ]),
                    correo=f"catedratico{i}@gmail.com",
                    telefono=f"4000{i:04d}"[:20],
                )
            )
        Catedratico.objects.bulk_create(catedraticos)
        catedraticos = list(Catedratico.objects.all())
        self.stdout.write(self.style.SUCCESS("100 catedráticos creados"))

        # 4. Asignaciones: 300
        secciones = ["A", "B", "C", "D"]
        ciclos = ["Primer Semestre 2026", "Segundo Semestre 2026"]
        asignaciones = []
        for _ in range(300):
            asignaciones.append(
                AsignacionCurso(
                    curso=random.choice(cursos),
                    catedratico=random.choice(catedraticos),
                    seccion=random.choice(secciones),
                    ciclo=random.choice(ciclos),
                )
            )
        AsignacionCurso.objects.bulk_create(asignaciones)
        asignaciones = list(AsignacionCurso.objects.all())
        self.stdout.write(self.style.SUCCESS("300 asignaciones creadas"))

        # 5. Inscripciones: 3000
        inscripciones = []
        for _ in range(3000):
            inscripciones.append(
                InscripcionAlumno(
                    alumno=random.choice(alumnos),
                    curso=random.choice(cursos),
                    fecha_inscripcion=self.generar_fecha_inscripcion(),
                    estado=random.choice(["Activa", "Retirada", "Finalizada"]),
                )
            )
        InscripcionAlumno.objects.bulk_create(inscripciones)
        inscripciones = list(InscripcionAlumno.objects.all())
        self.stdout.write(self.style.SUCCESS("3000 inscripciones creadas"))

        # 6. Calificaciones: 3500
        unidades = ["Unidad 1", "Unidad 2", "Unidad 3", "Proyecto Final"]
        calificaciones = []
        for _ in range(3500):
            calificaciones.append(
                Calificacion(
                    inscripcion=random.choice(inscripciones),
                    unidad=random.choice(unidades),
                    nota=Decimal(str(round(random.uniform(61, 100), 2))),
                    observacion=random.choice([
                        "Sin observación",
                        "Buen rendimiento",
                        "Debe reforzar contenidos",
                        "Excelente participación",
                    ]),
                )
            )
        Calificacion.objects.bulk_create(calificaciones)
        self.stdout.write(self.style.SUCCESS("3500 calificaciones creadas"))

        total = (
            Alumno.objects.count()
            + Curso.objects.count()
            + Catedratico.objects.count()
            + AsignacionCurso.objects.count()
            + InscripcionAlumno.objects.count()
            + Calificacion.objects.count()
        )

        self.stdout.write(self.style.SUCCESS(f"Proceso finalizado. Total de registros: {total}"))