# Generated by Django 2.2.2 on 2020-06-11 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TaskForce', '0006_auto_20200611_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='applications',
        ),
        migrations.AddField(
            model_name='task',
            name='applications',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to=settings.AUTH_USER_MODEL, verbose_name='Заявки'),
        ),
    ]
