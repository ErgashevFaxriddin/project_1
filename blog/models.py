from django.utils import timezone
from django.utils.text import slugify
from django.db import models
from django.utils.text import slugify


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
        on_delete=models.SET_NULL #agar author o'chirilsa, author maydoni NULL bo'ladi on_delete=models.CASCADE
                                  # #agar author o'chib ketsa book ha o'chib ketadi
        )
    genre = models.ForeignKey(Genre,
        null=True,
        on_delete=models.SET_NULL
        )

    def __str__(self):
        return self.name.title() #admin panelda foydalanuvchi ismi bilan korinish uchun

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True) #URL’ni o‘qilishi oson qilish uchun, , Masalan: https://mysite.com/blog/my-first-post → my-first-post bu slug.
    content = models.TextField()
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title #admin panelda foydalanuvchi ismi bilan korinish uchun

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)