from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()


class Category(models.Model):

  name = models.CharField(verbose_name='Наименование категории', max_length=255)

  def __str__(self):
    return f'Категория {self.name}'

  class Meta:
    verbose_name = 'Категорию'
    verbose_name_plural = 'Категории'

class Post(models.Model):

  name = models.CharField(verbose_name='Наименование поста', max_length=255)
  image = models.ImageField(verbose_name='Изображение', upload_to='posts/')
  content = models.TextField(verbose_name='Содержание поста', blank=True, null=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
  date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
  slug = models.SlugField(verbose_name='Наименование поста', unique=True)


  def __str__(self):
    return f'Пост {self.name}'

  def get_absolute_url(self):
    return reverse('post_detail', args=[str(self.slug)])

  class Meta:
    verbose_name = 'Пост'
    verbose_name_plural = 'Посты'


class Case(models.Model):

  name = models.CharField(verbose_name='Наименование кейса', max_length=255)
  image = models.ImageField(verbose_name='Изображение', upload_to='cases/')
  content = models.CharField(verbose_name='Содержание кейса', max_length=255, blank=True, null=True)
  slug = models.SlugField(verbose_name='Наименование кейса', unique=True)


  def __str__(self):
    return f'Кейс {self.name}'

  def get_absolute_url(self):
    return reverse('case_detail', args=[str(self.slug)])

  class Meta:
    verbose_name = 'Кейс'
    verbose_name_plural = 'Кейсы'
