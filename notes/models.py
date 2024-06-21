from django.db import models

class Note(models.Model): #Class for Notes
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Author(models.Model): #Author for Posts
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model): # Post Class itself
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
