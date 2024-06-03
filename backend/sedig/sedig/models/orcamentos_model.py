from django.db import models
from sedig.models import Usuario

class Orcamento(models.Model):
    nome_orcamento = models.CharField(max_length=255)
    nome_subestacao = models.CharField(max_length=255)
    macroregiao = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    ano_referencia = models.IntegerField()
    mes_referencia = models.CharField(max_length=255)
    tipo_instalacao = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Patio(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
    tensao_primaria = models.IntegerField()
    arranjo = models.CharField(max_length=255)

class ModuloManobra(models.Model):
    patio = models.ForeignKey(Patio, on_delete=models.CASCADE)
    sincronizacao_disjuntor = models.CharField(max_length=255)
    tipo_aplicacao = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    tipo = models.CharField(max_length=255)

class ModuloEquipamento(models.Model):
    patio = models.ForeignKey(Patio, on_delete=models.CASCADE)
    tipo_equipamento = models.CharField(max_length=255)
    quantidade = models.IntegerField()


