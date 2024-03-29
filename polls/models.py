import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("发布时间")

    def __str__(self):
        return self.question_text

    @admin.display(boolean=True, ordering="pub_date", description="最近发布？")
    def was_published_recently(self):
        return (
            self.pub_date >= timezone.now() - datetime.timedelta(days=1)
            and self.pub_date < timezone.now()
        )


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
