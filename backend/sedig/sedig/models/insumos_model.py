from django.db import models

class Insumo(models.Model):
    tipo_insumo = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    preco_unitario = models.FloatField()
    custo = models.FloatField()
    
