from django.contrib import admin
from .models import Familiares , Menues, Ubicaciones
from familiaapp.forms import familiaresformulario
# Register your models here.

admin.site.register(Familiares)
admin.site.register(Menues)
admin.site.register(Ubicaciones)
admin.site.register(familiaresformulario)