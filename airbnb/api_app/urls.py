from django.urls import path
from api_app import views

urlpatterns = [
    path('nivel/', views.niveis),
    path('nivel/<int:id>/', views.nivel),    
    path('produto/', views.produtos),
    path('produto/<int:id>/', views.produto),
    path('relacao/', views.relacoes),
    path('relacao/<int:id>/', views.relacao),
]