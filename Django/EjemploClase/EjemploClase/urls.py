"""
URL configuration for EjemploClase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
import contacs.views as contacs

urlpatterns = [
    path('holacomoestan', contacs.hola, name='hola'),
    path('admin/', admin.site.urls),
    path('', contacs.index, name='index'),
    path('contact/', contacs.list, name='contactlist'),
    path('contact/list', contacs.list, name='contactlist'),
    path('contact/<int:id>', contacs.retrieve, name='contactretrieve'),
    path('contact/create', contacs.create, name='contactcreate'),
    path('contact/store', contacs.store, name='contactstore'),
    path('contact/edit/<int:id>', contacs.edit, name='contactedit'),
    path('contact/update/<int:id>', contacs.update, name='contactupdate'),
    path('contact/delete/<int:id>', contacs.delete, name='contactdelete')
]
