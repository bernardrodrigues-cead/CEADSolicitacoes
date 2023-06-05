from django.contrib import admin
from django.apps import apps
from .models import EquipamentoProducaoDeMaterial, ProducaoDeMaterial, ServicoProducaoDeMaterial

# Obtenha todos os modelos do seu aplicativo
app_models = apps.get_app_config('SolicitacoesApp').get_models()

# Registre cada modelo no admin
for model in app_models:
    admin.site.register(model)