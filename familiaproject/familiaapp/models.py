from django.db import models
import uuid
# Create your models here.
class Familiares (models.Model):
    id = models.CharField(default= uuid.uuid4(),primary_key=True, max_length=100)
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    cumpleaños = models.DateField()
    email= models.EmailField()

class Menues(models.Model):
    id = models.CharField(default= uuid.uuid4(),primary_key=True, max_length=100)
    menue = models.CharField(max_length=50)
    
class Ubicaciones (models.Model):
    mesa =  models.IntegerField()
    invitacion = models.CharField(max_length=50)
    email= models.EmailField()
