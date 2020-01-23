"""
Definition of urls for informatic1024_03.
"""

from django.conf.urls.static import static
from app.views import gallery
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from datetime import datetime
from informatic1024_03 import urls
from app.views import registration
from app import views
from informatic1024_03 import settings
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

from django.conf.urls.static import static#Работа со статическими файлами (CSS, изображения)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns#собирает статические файлы со всех ваших приложений


# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^registration$', app.views.registration, name='registration'),
    url(r'^blog$', app.views.blog, name='blog'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^links$', app.views.links, name='links'),
    url(r'^(?P<parametr>\d+)/$', app.views.blogpost, name='blogpost'),
    url(r'^newpost$', app.views.newpost, name='newpost'),
    url(r'^gallery$', app.views.gallery, name='gallery'),
    url(r'^video$', app.views.video, name='video'),
    url(r'^bibliotek$', app.views.bibliotek, name='bibliotek'),
    url(r'^cursach$', app.views.cursach, name='cursach'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Вход',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   urlpatterns += staticfiles_urlpatterns() 
 