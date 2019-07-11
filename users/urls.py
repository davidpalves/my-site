# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.UserViewSet, base_name='user')

urlpatterns = router.urls
