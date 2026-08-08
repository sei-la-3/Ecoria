from django.urls import path
from . import views

urlpatterns = [
    path("", views.acesso, name="acesso"),
    path("cadastro/", views.cadastro, name="cadastro"),
]