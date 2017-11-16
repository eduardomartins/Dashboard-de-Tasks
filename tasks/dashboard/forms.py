# coding: UTF-8

from django import forms
from models import Task, Anexo


class TaskForm(forms.ModelForm):
    """ """
    class Meta:
        model = Task
        exclude = ('finalizada_por', 'criado_por', 'status')


class AnexoForm(forms.ModelForm):
    """ """
    class Meta:
        model = Anexo
        exclude = ('tarefa',)
        widgets = {
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
        }