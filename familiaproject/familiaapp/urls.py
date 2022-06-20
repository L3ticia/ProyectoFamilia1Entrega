
from django.urls import  path, include
from familiaapp import views



urlpatterns = [
    path  ('',  views.inicio),
    path  ('familiares', views.Familiares, name = "familiares"),
    path  ('menue', views.Menues, name = "menues"),
    path  ('ubicación', views.Ubicaciones),
    path  ('familiaresformulario', views.familiaresformulario, name ="familiaresformulario"),
   ]
