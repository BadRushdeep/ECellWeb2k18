# Generated by Django 2.0.5 on 2018-05-18 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='Test', max_length=200, verbose_name='title'),
            preserve_default=False,
        ),
    ]
