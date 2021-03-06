# Generated by Django 2.0.5 on 2018-05-18 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin', models.TextField(blank=True, max_length=64, null=True)),
                ('facebook', models.TextField(blank=True, max_length=64, null=True)),
                ('status', models.BooleanField()),
                ('contact_no', models.TextField(max_length=13)),
                ('avatar', models.ImageField(upload_to='static/uploads/avatar')),
                ('user_type', models.CharField(choices=[('GST', 'Guest'), ('VLT', 'Voluteer'), ('EXE', 'Executive'), ('MNG', 'Manager'), ('HC', 'Head Co-ordinator'), ('OC', 'Overall Co-ordinator')], default='GST', max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
