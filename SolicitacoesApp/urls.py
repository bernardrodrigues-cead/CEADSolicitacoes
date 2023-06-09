from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name='index'),
    path('producao/new/', views.ProducaoDeMaterialCreateView.as_view(), name="producao_create"),
    path('administracao/', views.MenuAdministracao, name="administracao"),
    path('administracao/viagens/new/', views.ViagensCreateView.as_view(), name='viagens_create'),
    path('administracao/almoxarifado_grafica/new/', views.AlmoxarifadoGraficaCreateView.as_view(), name='almoxarifado_grafica_create'),
    # Adicione outras URLs se necessário
]
