from django.db import models


# pip install djangorestframework
class Book(models.Model):
    title = models.CharField(max_length=100)
    page_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField()
