from django.utils import timezone
from django.utils.text import slugify
from django.db import models

# --------------------------
# Author model
# --------------------------
class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name.title()


# --------------------------
# Genre model
# --------------------------
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name.title()


# --------------------------
# Book model
# --------------------------
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    genre = models.ForeignKey(
        Genre,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name.title()


# --------------------------
# Post model
# --------------------------
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
