# Generated by Django 3.1.2 on 2020-11-17 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0007_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['id'], 'verbose_name': 'MiPersona'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombres y Apellidos'),
        ),
    ]
