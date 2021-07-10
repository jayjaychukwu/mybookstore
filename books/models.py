from django.db import models

# Create your models here.
class Book(models.Model):
    BookName = models.CharField('Name of Book',max_length=200, null=True)
    Author = models.CharField(max_length=200, null=True)
    Genre = models.CharField(max_length=200, null=True)
    Language = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.BookName