from core import views
from django.urls import path
from .views import index
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index')
]