from django.contrib import admin
from .models import EquipamentoProducaoDeMaterial, ProducaoDeMaterial, ServicoProducaoDeMaterial

# Register your models here.
admin.site.register(EquipamentoProducaoDeMaterial)
admin.site.register(ServicoProducaoDeMaterial)
admin.site.register(ProducaoDeMaterial)


