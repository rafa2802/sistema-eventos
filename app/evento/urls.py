from django.urls import path
from . import views as evento

app_name = 'evento'

urlpatterns = [
    path('', evento.HomeView.as_view(), name = 'home'),
    path('sucesso/<pk>', evento.Sucesso.as_view(), name = 'sucesso'),
    path('evento/<pk>/detalhes/', evento.EventoAdmin.as_view(), name = 'evento-detalhe-adm'),
    path('adicionar/palestrante/<pk>', evento.AddPalestrante.as_view(), name = 'add-palestrante'),
    path('adicionar/atividade/<pk>', evento.AddAtividade.as_view(), name = 'add-atividade'),
    path('detalhes/<pk>', evento.EventoDetalhe.as_view(), name = 'evento-detalhe'),
    path('evento/<pk>/excluir', evento.ExcluirEvento.as_view(), name = 'excluir-evento'),
    path('evento/<pk>/editar', evento.EditarEvento.as_view(), name = 'editar-evento'),
    path('atividade/<pk>/detalhes', evento.AtividadeAdmin.as_view(), name = 'detalhes-atividade'),
    path('atividade/<pk>/editar', evento.EditarAtividade.as_view(), name = 'editar-atividade'),
    path('atividade/<pk>/excluir', evento.ExcluirAtividade.as_view(), name = 'excluir-atividade'),
    path('atividade/<pk>/lista', evento.GerarLista.as_view(), name = 'gerar-lista'),
    path('user/<pk>/eventos/participo', evento.Participando.as_view(), name = 'participando'),
    path('user/<pk>/increver/atividade', evento.Inscrever.as_view(), name = 'inscrever'),
    path('user/<pk>/cancelar/inscricao', evento.Cancelar.as_view(), name = 'cancelar'),
]