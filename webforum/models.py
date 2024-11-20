from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Category: {self.name}'

class Tread(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='treads')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='treads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Tread: {self.name}'

class Post(models.Model):
    tread = models.ForeignKey(Tread,on_delete=models.CASCADE,related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    text = models.TextField()
    parent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Author: {self.author}, At: {self.created_at}'
