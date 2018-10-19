from django import forms

from .models import Atividade

class AddAtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ('palestrante', 'nome', 'duracao', 'data', 'hora', 'tipo')
        labels = {
            'palestrante': 'Palestrante',
            'nome': 'Nome da Atividade',
            'duracao': 'Duração da Atividade',
            'data': 'Data da Atividade',
            'hora': 'Hora da Atividade',
            'tipo': 'Tipo de Atividade',
        }
        widgets = {
            'data': forms.DateInput(),
            'hora': forms.TimeInput(),
            'duracao': forms.TimeInput(),
        }