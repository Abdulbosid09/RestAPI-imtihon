# Generated by Django 5.0.7 on 2024-07-14 09:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_darsvideosi_dars_videosi'),
    ]

    operations = [
        migrations.AddField(
            model_name='dars',
            name='dars_videosi',
            field=models.FileField(default=1, upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'MOV', 'AVI', 'MVB'])]),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DarsVideosi',
        ),
    ]
