from django.db import models

# Create your models here.


class Book(models.Model):
    # what are the "columns" inside the Book table
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)

    # to-string
    def __str__(self):
        return self.title + " - " + self.ISBN


class Publisher(models.Model):
    # what are the columns (aka. fields) inside the Publisher table
    name = models.CharField(blank=False, max_length=255)
    email = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    dob = models.DateField(blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name