import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

        
class Word_sta(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    word_text = models.CharField(max_length=200)
    levels = models.IntegerField(default=0)
    def __str__(self):
        return self.word_text
        
class Word_gen(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    word_text = models.CharField(max_length=200)
    levels = models.IntegerField(default=0)
    def __str__(self):
        return self.word_text