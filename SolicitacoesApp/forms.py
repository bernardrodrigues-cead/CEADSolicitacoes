from django import forms

from SolicitacoesApp.models import  MaterialConsumo, ImpressaoProvasApostilas, CortePapel, DadosDoPreposto, DadosDaViagem

class DadosDoPrepostoForm(forms.ModelForm):
    class Meta:
        model = DadosDoPreposto
        fields = '__all__'

class DadosDaViagemForm(forms.ModelForm):
    class Meta:
        model = DadosDaViagem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_saida'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['horario_saida'].widget = forms.TimeInput(attrs={'type': 'time'})
        self.fields['data_retorno'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['horario_retorno'].widget = forms.TimeInput(attrs={'type': 'time'})

class MaterialConsumoForm(forms.ModelForm):
    class Meta:
        model = MaterialConsumo
        fields = ['material_solicitado', 'quantidade', 'observacoes']

class ImpressaoProvasApostilasForm(forms.ModelForm):
    class Meta:
        model = ImpressaoProvasApostilas
        fields = ['arquivo', 'quantidade_provas_apostilas', 'separar_por_polos', 'localizacao_polo', 'observacoes']

class CortePapelForm(forms.ModelForm):
    class Meta:
        model = CortePapel
        fields = ['altura_papel_mm', 'largura_papel_mm', 'quantidade', 'observacoes']
