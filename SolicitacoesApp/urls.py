from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name='index'),
    path('producao/new/', views.ProducaoDeMaterialCreateView.as_view(), name="producao_create"),
    path('administracao/', views.MenuAdministracao, name="administracao"),
    path('administracao/viagens/new/', views.ViagensCreateView.as_view(), name='viagens_create'),
    path('solicitacao_almoxarifado/create/', views.CreateSolicitacaoAlmoxarifadoGraficaView.as_view(), name='create-solicitacao'),
    # Adicione outras URLs se necessário
]
