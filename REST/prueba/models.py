from django.db import models

# Create your models here.

class Usuario(models.Model):
    genero = (('M', 'Masculino'), ('F', 'Femenino'))
    nombre = models.CharField(max_length = 50)
    documento = models.IntegerField()
    ficha = models.IntegerField()
    programa = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50)
    genero = models.CharField(choices = genero, max_length = 50)
    photo = models.ImageField(upload_to='fotos/')

    def __str__(self):
        #return f"{self.nombre} {self.ficha}"
        return self.nombre
