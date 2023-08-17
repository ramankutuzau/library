from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Автор № {self.pk} Имя: {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

# class BookHistory()
class Book(models.Model):
    in_stock = models.BooleanField(default=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'Книга № {self.pk} Название: {self.title}, Автор: {self.author}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'




class Reader(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Отчество')

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"


class HistoryBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    reader = models.ForeignKey(Reader, on_delete=models.SET_NULL, blank=True, null=True)
    datetime_get = models.DateTimeField(auto_now_add=True)
    datetime_return = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return f'Книга № {self.book.pk} Название: {self.book.title}, Читатель: {self.reader.last_name} {self.datetime_get}/ {self.datetime_put}'

    class Meta:
        verbose_name = 'История книг'
        verbose_name_plural = 'История книг'