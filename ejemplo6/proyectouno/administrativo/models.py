from django.db import models

# Create your models here.

class Estudiante(models.Model):
    opciones_tipo_estudiante = (
        ('becado', 'Estudiante Becado'),
        ('no-becado', 'Estudiante No Becado'),
    )

    nombre = models.CharField("Nombre de estudiante", max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField("edad de estudiante")  # Verbose field names
    tipo_estudiante = models.CharField(max_length=30, choices=opciones_tipo_estudiante)
    modulos = models.ManyToManyField('Modulo', through='Matricula')

    def __str__(self):
        return "%s - %s - %s - edad: %d - tipo: %s" % (self.nombre,
                                                     self.apellido,
                                                     self.cedula,
                                                     self.edad,
                                                     self.tipo_estudiante)

    def calcular_costo_total(self):
        """
        Calcula el costo total de las matrículas asociadas a este estudiante.
        """
        total_costo = 0
        for matricula in self.lasmatriculas.all():
            total_costo += matricula.costo
        return total_costo


    def obtener_matriculas(self):
        return self.lasmatriculas.all()
        

class Modulo(models.Model):
    """
    """
    opciones_modulo = (
        ('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
        ('4', 'Cuarto'),
        ('5', 'Quinto'),
        ('6', 'Sexto'),
        )

    nombre = models.CharField(max_length=30, \
            choices=opciones_modulo)
    estudiantes = models.ManyToManyField(Estudiante, through='Matricula')

    def __str__(self):
        return "Módulo: %s" % (self.nombre)

class Costo(models.Model):
    matricula = models.OneToOneField('Matricula', on_delete=models.CASCADE, related_name='costo_asociado')
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Costo de matrícula para {self.matricula.estudiante.nombre} en {self.matricula.modulo.nombre}: {self.costo}"


class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, related_name='lasmatriculas', on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, related_name='lasmatriculas', on_delete=models.CASCADE)
    comentario = models.CharField(max_length=200)
    costo = models.DecimalField(max_digits=10, decimal_places=2)  # Campo para almacenar el costo de la matrícula

    def __str__(self):
        return f"Matricula: Estudiante({self.estudiante.nombre}) - Modulo({self.modulo.nombre})"
