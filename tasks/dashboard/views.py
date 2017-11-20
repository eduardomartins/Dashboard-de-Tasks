# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from models import Task, Anexo
from forms import TaskForm, AnexoForm


from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """ """
    tarefa = None
    form_task = TaskForm()
    form_anexo = AnexoForm()

    if request.method == 'POST':
        
        form_task = TaskForm(request.POST)
        form_anexo = AnexoForm(request.POST, request.FILES)
        
        if form_task.is_valid() and form_anexo.is_valid():
            form_task.instance.criado_por = request.user
            tarefa = form_task.save()
            
            for arq in request.FILES.getlist('anexos'):
                anx = Anexo(arquivo=arq, tarefa=tarefa)
                anx.save()
          
            return redirect(reverse('dashboard:index'))

    tarefas = Task.objects.all()
    dados = dict(
        processadas=tarefas.filter(status="processada"),
        finalizadas=tarefas.filter(status="done"),
        tefarefa=tarefa,
        tarefas=tarefas,
        form_task=form_task,
        form_anexo=form_anexo,
    )
    return render(request, 'dashboard_index.html', dados)


@login_required
def editar(request, pk):
    """ """
    salvo = None
    tarefa = tarefa = get_object_or_404(Task, id=pk)
    form_task = TaskForm(instance=tarefa)
    form_anexo = AnexoForm()

   
    if request.method == 'POST':
        form_task = TaskForm(request.POST, instance=tarefa)
        form_anexo = AnexoForm(request.POST, request.FILES)
        if form_task.is_valid() and form_anexo.is_valid():
            form_task.instance.criado_por = request.user
            salvo = form_task.save()

            for arq in request.FILES.getlist('anexos'):
                anx = Anexo(arquivo=arq, tarefa=tarefa)
                anx.save()

    dados = dict(
        salvo=salvo,
        tarefa=tarefa,
        form_task=form_task,
        form_anexo=form_anexo,
    )
    return render(request, 'dashboard_editar.html', dados)



@login_required
def excluir(request, pk):
    """ """
    tarefa = get_object_or_404(Task, id=pk)
    tarefa.delete()
    return redirect(reverse("dashboard:index"))



@login_required
def excluir_anexo(request, pk):
    """ """

    anexo = get_object_or_404(Anexo, id=pk)
    anexo.delete()
    return redirect(reverse("dashboard:editar-tarefa", kwargs=dict(pk=anexo.tarefa.id)))   