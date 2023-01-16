from django.db import models
import uuid
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
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    bixo_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_da_aposta = models.DateField(auto_now=True)
    hora_da_aposta = models.TimeField(auto_now_add=True)

    valor_apostado = models.FloatField(default=1)

    class Meta:
        verbose_name = 'Grupo'

class ApostasDuque(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    primeiro_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='primeiro_duque')
    segundo_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='segundo_duque')
    
    data_da_aposta = models.DateField(auto_now=True)
    hora_da_aposta = models.TimeField(auto_now_add=True)

    valor_apostado = models.FloatField(default=10,
        validators=[
            MinValueValidator(10)
        ])
    
    class Meta:
        verbose_name = 'Duque'

class ApostasTerno(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    primeiro_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='primeiro_terno')
    segundo_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='segundo_terno')
    terceiro_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='terceiro_terno')
    data_da_aposta = models.DateField(auto_now=True)
    hora_da_aposta = models.TimeField(auto_now_add=True)

    valor_apostado = models.FloatField(default=15,
        validators=[
            MinValueValidator(15)
        ])

    class Meta:
        verbose_name = 'Terno'

class ApostasQuadra(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    primeiro_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='primeiro_quadra')
    segundo_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='segundo_quadra')
    terceiro_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='terceiro_quadra')
    quarto_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='quarto_quadra')
    data_da_aposta = models.DateField(auto_now=True)
    hora_da_aposta = models.TimeField(auto_now_add=True)

    valor_apostado = models.FloatField(default=20,
        validators=[
            MinValueValidator(20)
        ])


    class Meta:
        verbose_name = 'Quadra'
    

class ApostasQuina(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    primeiro_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='primeiro_quina')
    segundo_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='segundo_quina')
    terceiro_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='terceiro_quina')
    quarto_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='quarto_quina')
    quinto_num_apostado = models.ForeignKey(Animais, on_delete=models.CASCADE, related_name='quinto_quina')
    data_da_aposta = models.DateField(auto_now=True)
    hora_da_aposta = models.TimeField(auto_now_add=True)

    valor_apostado = models.FloatField(default=25,
        validators=[
            MinValueValidator(25)
        ])

    class Meta:
        verbose_name = 'Quina'
    
class Sorteios(models.Model):
    sorteio_do_dia = models.IntegerField(default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(4)
        ])
    data_do_sorteio = models.DateField(auto_now=True)
    hora_do_sorteio = models.TimeField(auto_now_add=True)

    bixo_sorteado = models.ForeignKey(Animais, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'Sorteio'

class RandomFrases(models.Model):
    texto = models.TextField()