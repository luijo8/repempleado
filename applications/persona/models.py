from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return f'Habilidad: {self.id} - {self.habilidad}'

class Empleado(models.Model):
    """Modelo para tabla empleado"""
    JOB_CHOICES=(
        ('0','Contador') ,
        ('1','Administrador') ,
        ('2','Economista') ,
        ('3','Otro')     
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres y Apellidos', 
        max_length=120,
        blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    #departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    #departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null = True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    
    class Meta:
        verbose_name='MiPersona'
        ordering=['id']
        unique_together=('first_name','last_name')
    
    def __str__(self):
        return f'{self.id} - {self.first_name} - {self.last_name}'