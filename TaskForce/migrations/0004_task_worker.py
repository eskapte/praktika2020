# Generated by Django 2.2.2 on 2020-06-11 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TaskForce', '0003_auto_20200611_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='worker',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
    ]
