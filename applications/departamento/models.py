from django.db import models

# Create your models here.
class Departamento(models.Model):
    """Modelo para tabla departamento"""    
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado',default = False)
    
    class Meta:
        verbose_name='MiDepartamento'
        #verbose_name_plural='Areas de la empresa'
        #-name orden inverso
        ordering=['name']
        #No permite repetir la combinación de name y shor_name
        unique_together=('name','shor_name')
            
    def __str__(self):
        return f'Depatamento: {self.id} - {self.name} - {self.shor_name} - {self.anulate}'