from django.urls import path
from Lab01.views import suma,resta,multiplica
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('sumar/<int:num1>/<int:num2>',suma),
    path('restar/<int:num1>/<int:num2>',resta),
    path('multiplicar/<int:num1>/<int:num2>',multiplica),
]

