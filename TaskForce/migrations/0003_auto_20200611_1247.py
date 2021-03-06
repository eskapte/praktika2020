# Generated by Django 2.2.2 on 2020-06-11 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TaskForce', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='TaskForce/tasks/', verbose_name='Загруженные файлы'),
        ),
        migrations.AlterField(
            model_name='document',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='TaskForce.Task', verbose_name='Задание'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='icon',
            field=models.ImageField(default='TaskForce/user_icons/default_icon.jpg', upload_to='TaskForce/user_icons/', verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
