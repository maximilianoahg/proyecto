# Generated by Django 4.1.2 on 2024-06-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_remove_service_image_path_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/servicios/'),
        ),
    ]
