"""
URL configuration for RegistroPerritos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from perritos import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('propietarios/', views.PropietariosListView.as_view(), name='propietarios-list'),
    path('propietarios/<int:pk>/detail/', views.PropietariosDetailView.as_view(), name='propietarios-detail'),
    path('perritos/', views.PerritosListView.as_view(), name='perritos-list'),
    path('perritos/<int:pk>/detail/',views.PerritosDetailView.as_view(), name='perritos-detail'),
    path('raza/', views.RazaListView.as_view(), name='raza-list'),
    path('raza/<int:pk>/detail/',views.RazaDetailView.as_view(), name='raza-detail'),
   
]
