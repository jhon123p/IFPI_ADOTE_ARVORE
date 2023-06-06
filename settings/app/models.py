from django.db import models

# Create your models here.
class arvoreDetalhe(models.Model):
   nome = models.CharField(max_length=10)
   cod_planta = models.AutoField( primary_key=True)
   data_cadastro = models.DateField()
   observaçao = models.CharField(null=True , max_length=25)


class controleEntrega(models.Model):
    nome = models.CharField(max_length=10)
    codRegistro = models.ForeignKey(arvoreDetalhe , on_delete=models.CASCADE)
    contato = models.CharField(max_length=12)
    endereco = models.CharField(max_length=30)
    cidade = models.CharField(max_length=10)
    estado = models.CharField(max_length= 10)
    data_adicao = models.DateTimeField()
    data_plantio = models.DateField()
    qtdPlanta = models.IntegerField()
    local_plantio = models.CharField(max_length=15)
    
    

#def __str__(self):
    #return self.nome_completo