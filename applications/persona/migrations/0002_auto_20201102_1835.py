# Generated by Django 3.1.2 on 2020-11-03 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_auto_20201102_1831'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento'),
        ),
    ]