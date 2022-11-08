from email.policy import default
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    id_item = models.UUIDField(primary_key= True, default=uuid4, editable=False)
    nome = models.CharField(max_length = 180)
    descricao = models.CharField(max_length = 180)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    disponivel = models.BooleanField(default = False, blank = True)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    CREDITO = 1
    DEBITO = 2
    DINHEIRO = 3
    PIX = 4

    forma_pgt = (
        (CREDITO, 'Crédito'),
        (DEBITO, 'Débito'),
        (DINHEIRO, 'Dinheiro'),
        (PIX, 'Pix'),
    )

    venda_id = models.UUIDField(primary_key= True, default=uuid4, editable=False)
    item = models.ManyToManyField(Item, blank=True)
    quantidade = models.IntegerField(default=0, blank=True)
    modalidade = models.PositiveSmallIntegerField(choices=forma_pgt, default=DINHEIRO)