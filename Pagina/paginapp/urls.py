from django.urls import path
from.views import home, indice
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    #path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('', home, name='home'),
    path('inicio/', LoginView.as_view(template_name='inicio.html'), name='inicio'),
    path('register/', views.register_view, name='register'),
    path('indice/', views.indice, name='indice'),

]
