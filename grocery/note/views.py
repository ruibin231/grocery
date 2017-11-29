# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from grocery.note.models import Content, Tags
from grocery.note.forms import LoginForm, NoteForm


def home(request):
    notes = Content.objects.all()
    return render(request, 'note/home.html', {'notes': notes})


def user_login(request):
    next_url = request.GET.get('next', '')
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect('home')
    ctx = {
        'login_form': login_form,
        'next_url': next_url,
    }
    return render(request, 'login.html', ctx)


def user_logout(request):
    pass


@login_required
def new_note(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            user = request.user
            note.author = user
            note.save()
            return redirect(reverse('note_detail', args=(note.id, )))
    ctx = {'form': form}
    return render(request, 'note/new.html', ctx)


def note_detail(request, note_id):
    note = get_object_or_404(Content, pk=note_id)
    ctx = {'note': note}
    return render(request, 'note/note_detail.html', ctx)
