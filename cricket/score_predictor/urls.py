from django.urls import path
from . import views

app_name = 'score_predictor'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('form/', views.form, name='form')
]