from django.contrib.auth.models import User
from django.db import models


class CustomUser(User):
    patronymic = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Автор № {self.pk} Имя: {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Книга № {self.pk} Название: {self.title}, Автор: {self.author}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Reader(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)

    def __str__(self):
        return f'Читатель № {self.first_name} Название: {self.last_name}, Автор: {self.second_name}'

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'
