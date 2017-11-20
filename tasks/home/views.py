# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect


from django.contrib.auth import logout as lg
from django.contrib.auth.decorators import login_required



def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard:index'))
    return render(request, 'login.html')


def logout(request):
    lg(request)

    if 'next' in request.GET:
        return redirect(request.GET.get('next') or reverse('home'))
    
    return redirect(reverse('home'))

   
@login_required
def cadastro(request):
    return render(request, 'login.html')