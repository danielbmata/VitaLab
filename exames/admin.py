from django.contrib import admin
from .models import TiposExames, SolicitacaoExame, PedidosExames

#registando a model na area administrativa
admin.site.register(TiposExames)
admin.site.register(SolicitacaoExame)
admin.site.register(PedidosExames)
