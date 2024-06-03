from django.db import models

# Create your models here.
class TipoComida(models.Model):
    NomTipo = models.CharField(max_length=100)

    def __str__(self):
        return self.NomTipo

class Comida(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True, verbose_name='ISBN', unique=True)
    Nombre = models.CharField(max_length=100)
    contenido = models.CharField(max_length=100)
    Tipo = models.ForeignKey(TipoComida,on_delete=models.CASCADE,related_name="Comida")

    def __str__(self):
        return f"{self.isbn} - {self.Nombre}"