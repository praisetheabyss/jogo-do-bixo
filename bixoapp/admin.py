from django.contrib import admin
from bixoapp.models import *

# Register your models here.
@admin.register(Animais)
class AnimaisAdmin(admin.ModelAdmin):
    list_display = ("nome", "numero")

@admin.register(Sorteios)
class SorteiosAdmin(admin.ModelAdmin):
    list_display = ("num_sorteado", "data_do_sorteio")

@admin.register(ApostasGrupo)
class ApostasGrupoAdmin(admin.ModelAdmin):
    list_display = ("num_apostado", "data_da_aposta")

@admin.register(ApostasDuque)
class ApostasDuqueAdmin(admin.ModelAdmin):
    list_display = ("primeiro_num_apostado", "segundo_num_apostado", "data_da_aposta")

@admin.register(ApostasTerno)
class ApostasTernoAdmin(admin.ModelAdmin):
    list_display = ("primeiro_num_apostado", "segundo_num_apostado", "terceiro_num_apostado", "data_da_aposta")

@admin.register(ApostasQuadra)
class ApostasQuadraAdmin(admin.ModelAdmin):
    list_display = ("primeiro_num_apostado", "segundo_num_apostado", "terceiro_num_apostado", "quarto_num_apostado", "data_da_aposta")

@admin.register(ApostasQuina)
class ApostasQuinaAdmin(admin.ModelAdmin):
    list_display = ("primeiro_num_apostado", "segundo_num_apostado", "terceiro_num_apostado", "quarto_num_apostado", "quinto_num_apostado", "data_da_aposta")
