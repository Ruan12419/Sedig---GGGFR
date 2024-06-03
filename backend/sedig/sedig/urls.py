"""
URL configuration for sedig project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('cadastro', views.cadastro, name='cadastro'),
     path('login', views.login_view, name='login'), 
     path('api/auth/status', views.check_authentication, name='check_authentication'),
     path('logout', views.logout_view, name='logout'),
     path('usuario', views.usuario_view, name='usuario'),
     path('cadastrarOrcamento', views.OrcamentoCompletoView.as_view(), name='cadastrarOrcamento'),
     path('orcamentos', views.lista_orcamentos, name='lista_orcamentos'),
     path('orcamentos/edit/<int:orcamento_id>/', views.edit_orcamento, name='edit_orcamento'),
     path('orcamentos/delete/<int:orcamento_id>/', views.delete_orcamento, name='delete_orcamento'),
     path('insumos/', views.ListaInsumosView.as_view(), name='lista_insumos'),
     path('insumos/add/', views.AdicionaInsumoView.as_view(), name='adiciona_insumo'),
     path('insumos/update/<int:id>/', views.AtualizaInsumoView.as_view(), name='atualiza_insumo'),
     path('insumos/delete/<int:id>/', views.DeletaInsumoView.as_view(), name='deleta_insumo'),
]
