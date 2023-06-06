from django.db import models

# Create your models here.
class arvoreDetalhe(models.Model):
   nome = models.CharField(max_length=10)
   cod_planta = models.AutoSlugField(populate_from='nome', unique=True, slugify_function=slugify)
   data_cadastro = models.DateField()
   observaçao = models.CharField(null=True)


class controleEntrega(models.Model):
    nome = models.CharField(max_length=10)
    contato = models.IntegerField(max_length=12)
    endereco = models.CharField(30)
    cidade = models.CharField(max_length=10)
    estado = models.CharField(max_length= 10)
    data_adicao = models.DateTimeField()
    data_plantio = models.DateField()
    qtdPlanta = models.IntegerField()
    local_plantio = models.CharField()
    