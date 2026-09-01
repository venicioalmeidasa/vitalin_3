from django.urls import path
from . import views

app_name = 'regional'

urlpatterns = [
    path('distritos/', views.DistritoList.as_view(), name='distritos'),
    path('distrito/<str:slug>/', views.DistritoDetail.as_view(), name='distrito')
]