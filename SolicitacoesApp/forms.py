from django import forms

from SolicitacoesApp.models import DadosDoPreposto, DadosDaViagem

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
        self.fields['data_retorno'].widget = forms.DateInput(attrs={'type': 'date'})