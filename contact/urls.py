# -*- coding: utf-8 -*-
from django.urls.conf import path
from contact import views


urlpatterns = [
    path('', views.ListContactView.as_view(), name="contact")
]
