from django.urls import path
from . import views

app_name = 'assistencial'

urlpatterns = [
    path('ubss/', views.Ubss.as_view(), name='ubss'),
    path('ubs/<str:slug>/', views.Ubs.as_view(), name='ubs')
]