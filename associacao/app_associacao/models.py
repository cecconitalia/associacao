from django.db import models
from django import forms 

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.CharField(max_length=300)    
