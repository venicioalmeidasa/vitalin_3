from os import name
from django.urls import path
from . import views

app_name = 'assistencial'

urlpatterns = [
    path('ubss/', views.UbssList.as_view(), name='ubss'),
    path('ubs/<str:slug>/', views.UbsDetail.as_view(), name='ubs'),
    path('especialidades/', views.EspecialidadesList.as_view(), name='especialidades'),
    path('especialidade/<str:slug>/', views.EspecialidadeDetail.as_view(), name='especialidade'),
    path('cecos/', views.CecosList.as_view(), name='cecos'),
    path('ceco/<str:slug>/', views.CecoDetail.as_view(), name='ceco')
]