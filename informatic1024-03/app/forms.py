"""
Definition of forms.
"""
from django.db import models
from.models import Comment
from .models import Blog

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Ваше имя:'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль:'}))


class CommentForm (forms.ModelForm):
   class Meta:
     model = Comment # используемая модель
     fields = ('text',) # требуется заполнить только поле text
     labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm (forms.ModelForm):
   class Meta:
     model = Blog # используемая модель
     fields = ('image','title','description','content','posted',) # требуется заполнить только поле text
