# Generated by Django 3.0.6 on 2020-06-09 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
    ]
