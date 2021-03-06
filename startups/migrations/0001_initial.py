# Generated by Django 2.0.4 on 2018-05-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('pic', models.ImageField(upload_to='Startups')),
                ('contact', models.TextField(blank=True, max_length=13, null=True)),
                ('founder', models.CharField(max_length=256)),
                ('address', models.TextField()),
                ('flag', models.BooleanField(default=False)),
            ],
        ),
    ]
