from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    CHAPTER_CHOICES = [
        ('nighttongue', 'NightTongue'),
        ('devnotes', 'Dev Notes'),
        ('otherramblings', 'Other Ramblings'),
        ('primeengine', 'Prime Engine'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    chapter = models.CharField(max_length=50, choices=CHAPTER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
