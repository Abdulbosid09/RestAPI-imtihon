# Generated by Django 5.0.7 on 2024-07-14 08:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_created_by_izoh_muallif_darsbahosi_muallif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darsvideosi',
            name='dars_videosi',
            field=models.FileField(upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'MOV', 'AVI', 'MVB'])]),
        ),
    ]
