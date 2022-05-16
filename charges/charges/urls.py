"""charges URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from charge.charges_views import ChargesView
from charge.views import CategoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', CategoryView.as_view(), name='CREATE'),
    path('read/<int:pk>', CategoryView.as_view(), name='READ_ONE'),
    path('update/<int:pk>', CategoryView.as_view(), name='UPDATE_ONE'),
    path('delete/<int:pk>', CategoryView.as_view(), name='DELETE_ONE'),
    path('read/', CategoryView.as_view(), name='READ')

]
"""Charges"""
urlpatterns+=[
    path('create_price/', ChargesView.as_view()),
    path('read_price/<int:pk>', ChargesView.as_view()),
    path('update_price/<int:pk>', ChargesView.as_view()),
    path('delete_price/<int:pk>', ChargesView.as_view()),
    path('delete_price/', ChargesView.as_view()),
    path('read_price/', ChargesView.as_view())

]
