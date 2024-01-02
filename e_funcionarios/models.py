from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=30)
    senha = models.CharField(max_length=64)

    def __str__(self):
        return self.nome