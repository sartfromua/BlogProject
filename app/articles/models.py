from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    article = models.ForeignKey('Article', on_delete=models.RESTRICT)

    def __str__(self):
        return self.text


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    text = models.TextField()
    image = models.CharField(max_length=300)
    publication_date = models.DateField()
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tag = models.ForeignKey(Tag, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title
