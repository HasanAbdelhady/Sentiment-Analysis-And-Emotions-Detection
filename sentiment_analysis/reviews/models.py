from django.db import models

class Review(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10)

    def __str__(self):
        return self.text
