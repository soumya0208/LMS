# Generated by Django 3.1.2 on 2020-12-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_delete_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoentry',
            name='video',
            field=models.FileField(null=True, upload_to='video/%y'),
        ),
    ]