from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return self.title


