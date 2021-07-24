from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Topic(models.Model):
    text = models.CharField(max_length=120)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('log_learnings:topic', args=[self.id])


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField() #separted the textfield sekof we want entry to be optional
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f'{self.text[:50]}...'
#% url 'log_learnings:topic' topic.pk %