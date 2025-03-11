from django.db import models
from django.contrib.auth.models import User
# Create your models here.    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.like_set.count()
    
    def total_comments(self):
        return self.comment_set.count()
    
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE,)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.content[:20]

class Category(models.Model):
    LIFESTYLE = 'Lifestyle'
    TECHNOLOGY = 'Technology'
    EDUCATION = 'Education'
    ENTERTAINMENT = 'Entertainment'
    
    CATEGORY_CHOICES = [
        (LIFESTYLE, 'Lifestyle'),
        (TECHNOLOGY, 'Technology'),
        (EDUCATION, 'Education'),
        (ENTERTAINMENT, 'Entertainment'),
    ]
    
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.name

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'

