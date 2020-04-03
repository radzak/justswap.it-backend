# -*- coding: utf-8 -*-

from django.urls import path

from justswap.main.views import index

# Place your URLs here:

app_name = 'main'

urlpatterns = [
    path('hello', index, name='hello'),
]
