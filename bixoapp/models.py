from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Animais(models.Model):
    nome = models.CharField(max_length=30)
    numero = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Animais'
        ordering = ('numero', 'nome')


class ApostasGrupo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    data_da_aposta = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Grupo'

class ApostasDuque(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    primeiro_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    segundo_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    data_da_aposta = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Duque'

class ApostasTerno(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    primeiro_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    segundo_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    terceiro_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    data_da_aposta = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Terno'

class ApostasQuadra(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    primeiro_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    segundo_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    terceiro_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    quarto_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    data_da_aposta = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Quadra'
    

class ApostasQuina(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    primeiro_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    segundo_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    terceiro_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    quarto_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    quinto_num_apostado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    data_da_aposta = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Quina'
    
class Sorteios(models.Model):
    data_do_sorteio = models.DateField(auto_now=True)
    num_sorteado = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])

    class Meta:
        verbose_name = 'Sorteio'