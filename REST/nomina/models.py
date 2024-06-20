from django.db import models

class Empleado(models.Model):
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    )
    
    TIPO_EMPLEADO_CHOICES = (
        ('Dependiente', 'Dependiente'),
        ('Independiente', 'Independiente')
    )

    NIVEL_RIESGO_CHOICES = (
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        ('V', 'V')
    )
    
    
    nombre = models.CharField(max_length=50)
    documento = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=200, default="")
    genero = models.CharField(choices=GENERO_CHOICES, max_length=1)
    photo = models.ImageField(upload_to='fotos/')
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_empleado = models.CharField(choices=TIPO_EMPLEADO_CHOICES, max_length=13)
    nivel_riesgo = models.CharField(choices=NIVEL_RIESGO_CHOICES, max_length=3)
    dias_trabajados = models.IntegerField(null=True, default=0)
    horas_semanales = models.IntegerField(default=0)
    hExtraDiurna = models.IntegerField(default=0)
    hExtraNocturna = models.IntegerField(default=0)
    hExtraDDominical = models.IntegerField(default=0)
    hExtraNDominical = models.IntegerField(default=0)
    hRecargoDominical = models.IntegerField(default=0)
    hRecargoNDominical = models.IntegerField(default=0)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre
