# coding: UTF-8

from django import forms
from models import Task, Anexo


class TaskForm(forms.ModelForm):
    """ """
    class Meta:
        model = Task
        exclude = ('finalizada_por', 'criado_por', 'status')


class AnexoForm(forms.Form):
    """ """
    anexos = forms.FileField(
        required=False,
        help_text="Selecione um ou mais arquivos",
        widget=forms.FileInput(attrs={'multiple': True})
    )

    