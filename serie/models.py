from django.db import models

# Create your models here.
class Serie(models.Model):
    nome = models.CharField(max_length=150)
    idGenero=models.ForeignKey('genero.Genero',on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


