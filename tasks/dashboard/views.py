# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from models import Task, Anexo
from forms import TaskForm, AnexoForm


from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.forms import modelform_factory
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    """ """
    tarefa = None
    form_task = TaskForm()

    AnexoFormSet = modelform_factory(   
        Anexo, 
        form=AnexoForm, 
    )

    formset_anexo = AnexoFormSet()

    if request.method == 'POST':
        form_task = TaskForm(request.POST)
        formset_anexo = AnexoFormSet(request.POST, request.FILES)
        if form_task.is_valid() and formset_anexo.is_valid():
            form_task.instance.criado_por = request.user
            tarefa = form_task.save()
            formset_anexo.instance.tarefa = tarefa 
            formset_anexo.save()

    dados = dict(
        tefarefa=tarefa,
        tarefas=Task.objects.all(),
        form_task=form_task,
        formset_anexo=formset_anexo,
    )
    return render(request, 'dashboard_index.html', dados)


@login_required
def editar(request, pk):
    """ """
    salvo = None
    tarefa = tarefa = get_object_or_404(Task, id=pk)
    form_task = TaskForm(instance=tarefa)
    #AnexoFormSet = inlineformset_factory(   
    #    Anexo, 
    #    form=AnexoForm, 
    #)

    #formset_anexo = AnexoFormSet(instance=tarefa.anexo_set.all())

    if request.method == 'POST':
        form_task = TaskForm(request.POST, instance=tarefa)
        #formset_anexo = AnexoFormSet(request.POST, request.FILES, queryset=tarefa.anexo_set.all())
        if form_task.is_valid(): #and formset_anexo.is_valid():
            #form_task.instance.criado_por = request.user
            salvo = form_task.save()
            #formset_anexo.instance.tarefa = tarefa 
            #formset_anexo.save()

    dados = dict(
        salvo=salvo,
        tefarefa=tarefa,
        form_task=form_task,
        #formset_anexo=formset_anexo,
    )
    return render(request, 'dashboard_editar.html', dados)


@login_required
def excluir(request, pk):
    """ """
    tarefa = get_object_or_404(Task, id=pk)
    tarefa.delete()
    return redirect(reverse("dashboard:index"))