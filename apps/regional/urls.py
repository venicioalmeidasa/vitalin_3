from django.urls import path
from . import views

app_name = 'regional'

urlpatterns = [
    path('distritos/', views.DistritoView.as_view(), name='distritos')
]