# Generated by Django 2.0 on 2018-02-13 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20180213_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='name',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='name',
        ),
    ]