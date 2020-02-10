import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') #날짜와 시간 필드
    def __str__(self):
        return self.question_text

    def was_published_recently(self):#pub_date시간이 현재시각 기준 하루가 안지났는지.
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 각각의 Choice 가 하나의 Question 에 관계된다.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

