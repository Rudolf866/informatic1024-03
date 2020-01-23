"""
Definition of views.
"""
from.forms import BlogForm
from.models import Comment
from app import forms # использование модели комментариев
from.forms import CommentForm # использование формы ввода комментария


from django.db import models
from .models import Blog

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
import django
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Kovalevskiy Rudolf Alexandrovich.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def links(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            
        }
    )
def registration(request):
 """Renders the registration page."""
 regform = UserCreationForm (request.POST)
 if request.method == "POST": # после отправки формы
     regform = UserCreationForm (request.POST)
 if regform.is_valid(): #валидация полей формы
     reg_f = regform.save(commit=False) # не сохраняем данные формы
     reg_f.is_staff = False # запрещен вход в административный раздел
     reg_f.is_active = True # активный пользователь
     reg_f.is_superuser = False # не является суперпользователем
     reg_f.date_joined = datetime.now() # дата регистрации
     reg_f.last_login = datetime.now() # дата последней авторизации

     reg_f.save() # сохраняем изменения после добавления данных (добавление пользователя в БД пользователей)

     return redirect('home')      # переадресация на главную страницу после регистрации
 else:
     regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя
 assert isinstance(request, HttpRequest) 
 return render(
 request,
 'app/registration.html',
 {

 'regform': regform, # передача формы в шаблон веб-страницы

 'year':datetime.now().year,
 }
 )
def blog(request):
 """Renders the blog page."""
 posts = Blog.objects.order_by('-posted') # запрос на выбор всех статей из модели, отсортированных по убыванию даты опубликования
 assert isinstance(request, HttpRequest)
 return render(
 request,
 'app/blog.html',
 { # параметр в {} — данные для использования в шаблоне.
 'title':'Блог',
 'posts': posts, # передача списка статей в шаблон веб-страницы
 'year':datetime.now().year
 }
 )
def blogpost(request, parametr):
 """Renders the blogpost page."""

 post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
 comments=Comment.objects.filter(post=parametr)
   
 if request.method=="POST":# после отправки данных формы на сервер методом POST
    form=CommentForm(request.POST)
    if form.is_valid():
        comment_f=form.save(commit=False)
        comment_f.author=request.user# добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
        comment_f.date=datetime.now() # добавляем в модель Комментария (Comment) текущую дату
        comment_f.post=Blog.objects.get(id=parametr)# добавляем в модель Комментария (Comment) статью, для которой данный комментарий
        comment_f.save()# сохраняем изменения после добавления полей
  
        return redirect('blogpost', parametr=post_1.id)# переадресация на ту же страницу статьи после отправки комментария
 else:
  form = CommentForm() # создание формы для ввода комментария
   

 assert isinstance(request, HttpRequest)
   
 return render(
 request,
 'app/blogpost.html',
 {
 'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы
 'form': form, # передача формы в шаблон веб-страницы 
 'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы
 'year':datetime.now().year,
 }
 
 )
def newpost(request):
    if request.method=="POST"and request.FILES:
     form = BlogForm(request.POST, request.FILES)
    
     if form.is_valid():
         
           cd = form.cleaned_data
           file = cd['image']
           title = cd['title']
           description = cd['description']
           content = cd['content']
           form.save()
     return redirect('blog')
    else:

        form = BlogForm()


    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/newpost.html',
        {
            'form': form
        }
    )
def gallery(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/gallery.html',
        {
            
        }
    )

def video(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/video.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def bibliotek(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/bibliotek.html',
        {
            
        }
    )

def cursach(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cursach.html',
        {
            
        }
    )