from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo/', views.novo_gastos, name='novo-gastos'),
    path('cadastro/', views.cadastro, name='cadastro'),
]