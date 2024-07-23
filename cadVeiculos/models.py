from django.db import models


class Veiculo(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    ano = models.IntegerField()
