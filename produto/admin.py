from django.contrib import admin
from . import models
#from .models import Produto,Variacao
#from .models import *


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1

class ProdutoAdmin(admin.ModelAdmin): #ITENS QUE VAO APARECER NO DISPLAY DO ADMIN
    list_display=['nome','descricao_curta','get_preco_formatado','get_preco_promocional_formatado']
    inlines = [
        VariacaoInline
    ]

admin.site.register(models.Produto,ProdutoAdmin)
admin.site.register(models.Variacao)
