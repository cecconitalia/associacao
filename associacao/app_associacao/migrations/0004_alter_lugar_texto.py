# Generated by Django 4.2.7 on 2023-11-09 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_associacao', '0003_alter_lugar_texto_alter_lugar_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='texto',
            field=models.TextField(max_length=200),
        ),
    ]
