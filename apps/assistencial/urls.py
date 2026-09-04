from django.urls import path
from . import views

app_name = 'assistencial'

urlpatterns = [
    path('ubss/', views.Ubss.as_view(), name='ubss'),
    path('ubs/<str:slug>/', views.Ubs.as_view(), name='ubs'),
    path('especialidades/', views.Especialidades.as_view(), name='especialidades'),
    path('especialidade/<str:slug>/', views.Especialidade.as_view(), name='especialidade')
]