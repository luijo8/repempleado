# Generated by Django 3.1.2 on 2020-11-05 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_auto_20201104_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades Empleados',
            },
        ),
    ]
