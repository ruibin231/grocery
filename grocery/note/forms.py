# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from grocery.note.models import Content


class LoginForm(forms.Form):
    username = forms.CharField(label=u'用户名',
                               error_messages={'required': u'请输入用户名'})
    password = forms.CharField(label=u'密码',
                               error_messages={'required': u'请输入密码'},
                               widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if not User.objects.filter(username=username).exists():
                self._errors['username'] = self.error_class(['用户不存在'])
        return username

    def clean(self):
        super(LoginForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            self._errors['password'] = self.error_class([u'密码错误，请重新填写'])
        self.cleaned_data['user'] = user
        return self.cleaned_data


class NoteForm(forms.ModelForm):

    class Meta:
        model = Content
        exclude = ('create_time', 'update_time', 'click_rate', 'author',
                   'desc', 'tags', )

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if not title:
            self._errors['title'] = self.error_class([u'请取个标题'])
        if len(title) > 72:
            self._errors['title'] = self.error_class([u'请使用小与72个字的标题'])
        return title

    def clean_context(self):
        context = self.cleaned_data.get('context', '')
        if not context:
            self._errors['context'] = self.error_class([u'请输入文章内容'])
        return context

    def clean(self):
        super(NoteForm, self).clean()
        return self.cleaned_data
