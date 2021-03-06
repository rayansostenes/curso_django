from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    nome = models.CharField(max_length=255)
    localidade = models.CharField(max_length=255)
    saudacao = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    filial_conveniada = models.CharField(max_length=255)
    conveniada = models.CharField(max_length=255)
    sequencia_conveniada = models.CharField(max_length=255)
    codigo_portal = models.CharField(max_length=255)
    contato_empresa = models.CharField(max_length=255)




class Phone(models.Model):
    class Meta:
        managed = False

    CARRIER_CHOICES = (
        (1, 'TIM'),
        (1, 'Claro'),
        (1, 'Oi'),
        (1, 'Vivo'),
    )
    number = models.CharField('Número', max_length=20)
    carrier = models.SmallIntegerField('Operadora', choices=CARRIER_CHOICES)

    def __str__(self):
        return self.number

class Person(models.Model):
    name = models.CharField('Nome', max_length=255)
    email = models.EmailField()
    phone = models.ManyToManyField(Phone, verbose_name='Telefone')
    # address = models.ManyToManyField(Address, verbose_name='Endereço')
    created_on = models.DateTimeField('Criado Em', auto_now_add=True)
    is_active = models.BooleanField('Ativo', default=False)

    # def get_absolute_url(self):
    #     from django.core.urlresolvers import reverse
    #     return reverse('', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name