# Generated by Django 2.0.6 on 2018-06-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0003_auto_20180521_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='flag',
            field=models.BooleanField(default=False),
        ),
    ]