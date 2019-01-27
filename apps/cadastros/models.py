# -*- coding: utf-8 -*-

from django.db import models


UF_SIGLA = [
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AP', 'AP'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('EX', 'EX'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MT', 'MT'),
    ('MS', 'MS'),
    ('MG', 'MG'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PR', 'PR'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SP', 'SP'),
    ('SE', 'SE'),
    ('TO', 'TO'),
]

class Endereco(models.Model):
    uf = models.CharField(max_length=3, null=True,
                          blank=True, choices=UF_SIGLA)
    cidade = models.CharField(max_length=64, null=True, blank=True)
    bairro = models.CharField(max_length=64, null=True, blank=True)
    logradouro = models.CharField(max_length=86, null=True, blank=True)
    pontoreferencia = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'Endereco_cad'
        verbose_name = "Endereco"
        verbose_name_plural = "Enderecos"

    def __unicode__(self):
        s = u'%s, %s, %s, %s (%s)' % (
            self.logradouro, self.pontoreferencia, self.bairro, self.cidade, self.uf)
        return s

    def __str__(self):
        s = u'%s, %s, %s, %s (%s)' % (
            self.logradouro, self.pontoreferencia, self.bairro, self.cidade, self.uf)
        return s



class Onibus(models.Model):

    numero = models.CharField(max_length=6, null=False, blank=False)
    empresa = models.CharField(max_length=50, help_text="Nome da Empresa")
    descricao = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = 'onibus_cad'
        verbose_name = "Onibus"
        verbose_name_plural = "Onibus"

    def __unicode__(self):
        s = u'%s, %s, %s' % (
            self.numero, self.empresa, self.descricao)
        return s

    def __str__(self):
        s = u'%s, %s, %s' % (
            self.numero, self.empresa, self.descricao)
        return s


class Parada(models.Model):
    onibus = models.ManyToManyField(Onibus)
    numero = models.CharField(max_length=6, null=True, blank=True)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'parada_cad'
        verbose_name = "Parada"
        verbose_name_plural = "Paradas"

    def __unicode__(self):
        s = u'%s, %s, %s' % (
            self.onibus, self.numero, self.endereco)
        return s

    def __str__(self):
        s = u'%s, %s, %s' % (
            self.onibus, self.numero, self.endereco)
        return s



class Destino(models.Model):

    parada = models.ManyToManyField(Parada)

    aprovado = models.BooleanField(default=False)

    class Meta:
        db_table = 'Destino_cad'
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"

    def __unicode__(self):
        s = u'%s, %s, %s' % (
            self.parada.onibus, self.parada.numero, self.parada.endereco)

        return s

    def __str__(self):
        s = u'%s, %s, %s' % (
            self.parada.onibus, self.parada.numero, self.parada.endereco)
        return s




