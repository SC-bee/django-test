from django.db import models
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


#質問
class Question(models.Model):
    #質問内容
    question_text = models.CharField(max_length=200)
    #公開日時
    pub_date = models.DateTimeField('date pulished')

    #__str__メソッド
    def __str__(self):
        return self.question_text

    #最近公開されたものか判別するメソッド
    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#質問の選択肢
class Choice(models.Model):
    #Question に紐づいた外部キー
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #選択肢の内容
    choice_text = models.CharField(max_length=200)
    #投票数
    votes = models.IntegerField(default=0)

    #__str__メソッド
    def __str__(self):
        return self.choice_text