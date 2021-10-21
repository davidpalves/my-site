# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from users.views import RegistrationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('contact/', include('contact.urls')),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('docs/', include_docs_urls(title='Blog API Documentation'))
]
