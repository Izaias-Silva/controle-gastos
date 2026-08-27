from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def _str_(self):
        return self.nome

class Gasto(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()

    def _str_(self):
        return f"{self.descricao} - R$ {self.valor}"


