# Generated by Django 2.2.14 on 2020-07-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbtemp_app', '0003_auto_20200726_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='files',
            field=models.FileField(upload_to='files'),
        ),
    ]
