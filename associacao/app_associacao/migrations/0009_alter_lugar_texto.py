# Generated by Django 4.2.7 on 2023-11-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_associacao', '0008_rename_id_lugar_id_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='texto',
            field=models.TextField(max_length=255),
        ),
    ]
