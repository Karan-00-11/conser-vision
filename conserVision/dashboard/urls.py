from django.contrib import admin
from django.urls import path, include

from . import views

app_name='dashboard'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('batch/', views.batch_predict, name='batch'),
    path('save_pdf/', views.GeneratePdf.as_view(), name='save_pdf'),
]
