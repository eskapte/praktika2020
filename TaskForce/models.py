from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    icon = models.ImageField('Иконка', upload_to='TaskForce/user_icons/',
                             default='TaskForce/user_icons/default_icon.jpg')
    is_customer = models.BooleanField('Заказчик', default=False)

    def __str__(self):
        return f"Профиль {self.user.username}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='tasks')
    worker = models.OneToOneField(User, on_delete=models.SET_NULL, verbose_name='Исполнитель', blank=True, null=True,
                                  related_name='worker')
    desc = models.TextField('Описание')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='Категория',
                                 related_name='task')

    cities = [
        ('moscow', 'Москва'),
        ("moscow_region", 'МО'),
        ('st-Petersburg', 'Санкт-Петербург'),
        ('krasnodar', 'Краснодар'),
        ('irkutsk', 'Иркутск'),
        ('vladivostok', 'Владивосток')
    ]

    statuses = [
        ('new', 'Новое'),
        ('canceled', 'Закрыто'),
        ('in_word', 'В работе'),
        ('completed', 'Выполнено'),
        ('failed', 'Провалено')
    ]

    status = models.CharField(max_length=100, verbose_name='Статус', choices=statuses, default='new')
    location = models.CharField(max_length=100, verbose_name='Локация', choices=cities)
    price = models.IntegerField('Бюджет', null=True, blank=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    period_of_execution = models.DateField('Срок исполнения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['-created']


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField('Заставка', upload_to='TaskForce/category_images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Document(models.Model):
    file = models.FileField('Загруженные файлы', upload_to="TaskForce/tasks/", blank=True, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задание", related_name='files',
                             blank=True, null=True)

    class Meta:
        verbose_name = 'Загруженный файл'
        verbose_name_plural = "Загруженные файлы"

    def __str__(self):
        return os.path.basename(self.file.name)


class Application(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='applications')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    text = models.CharField(max_length=255, default='Я хочу выполнить задание!')
    price = models.IntegerField(blank=True, null=True, verbose_name='Цена')
    created = models.DateTimeField(auto_now_add=True)