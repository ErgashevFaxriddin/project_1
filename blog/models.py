from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    link = models.URLField(null=True)

    def __str__(self):
        return self.name.title() #admin panelda foydalanuvchi ismi bilan korinish uchun


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name.title() #admin panelda foydalanuvchi ismi bilan korinish uchun


class Book(models.Model):
    name = models.CharField(max_length=100) #ism kiritish majburiy
    author = models.ForeignKey(
        Author,     #Author modeliga ForeignKey
        null=True,  #DBda NULL bo‘lishi mumkin
        on_delete=models.SET_NULL #agar author o'chirilsa, author maydoni NULL bo'ladi on_delete=models.CASCADE #agar author o'chib ketsa book ha o'chib ketadi
        )
    genre = models.ForeignKey(Genre,
        null=True,
        on_delete=models.SET_NULL
        )

    def __str__(self):
        return self.name.title() #admin panelda foydalanuvchi ismi bilan korinish uchun

