# Generated by Django 4.2.7 on 2023-11-11 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_associacao', '0006_rename_id_lugar_lugar_id_alter_lugar_texto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='texto',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='titulo',
            field=models.TextField(max_length=255),
        ),
    ]
