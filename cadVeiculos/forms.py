from django import forms
from crispy_forms.helper import FormHelper
from .models import Veiculo
from crispy_forms.layout import Submit


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'marca', 'ano']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.template_pack = 'bootstrap5'
        self.helper.add_input(Submit('submit', 'Salvar'))