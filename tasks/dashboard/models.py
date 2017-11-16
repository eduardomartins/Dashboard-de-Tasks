# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORIDADE = (
        (1, '1 - Mínima'),
        (2, '2 - Baixa'),
        (3, '3 - Normal'),
        (4, '4 - Alta'),
        (5, '5 - Urgente'),
    )
    STATUS = (
        ('processada', 'processada'),
        ('done', 'done'),
    )
    nome = models.CharField(
        verbose_name="Nome",
        max_length=140,
    )
    descricao = models.TextField(
        verbose_name="Descrição",
        blank=True, 
        null=True
    )
    prioridade = models.PositiveIntegerField(
        choices=PRIORIDADE, 
        default=3
    )
    status = models.CharField(
        choices=STATUS,
        max_length=64   ,
        default="Processada",
    )
    finalizada_por = models.ForeignKey(
        User,
        verbose_name="Finalizada por",
        related_name="tarefas_finalizada",
        null=True, 
        blank=True,
    ) 
    criado_por = models.ForeignKey(
        User,
        verbose_name="Criada por",
    )
    data_criacao = models.DateTimeField(
        verbose_name="Data de criação",
        auto_now_add = True,
    )
    data_modificacao = models.DateTimeField(
        verbose_name="Data de modificação",
        auto_now = True,
    )


def user_directory_path(instance, filename):
    return os.path.join('anexos', filename)

class Anexo(models.Model):
    tarefa = models.ForeignKey(Task)
    arquivo = models.FileField(upload_to=user_directory_path)
