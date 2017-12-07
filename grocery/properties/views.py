# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from grocery.properties.models import Category, Assets, AssetsImg, Comment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'index.html', {})

def asset_add(request):
    pass

def asset_delete(request):
    pass

def asset_update(request):
    pass

def asset_detail(request):

    return 
@csrf_exempt
def categroy_add(request):
    name = request.POST.get('name')
    if Category.objects.get_or_create(name=name)[1]:
        return JsonResponse({'success': True, 'status': 2001})
    return JsonResponse({'success': False, 'status': 4001})

def categroy_get(request):
    pass

def categroy_delete(request):
    pass

def categroy_update(request):
    pass

