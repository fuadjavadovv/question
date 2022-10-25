from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def how_question(self):
      regard = self.quizs.count()
      return  regard

class Question(models.Model):
    # quiz = models.ForeignKey(Quiz,on_delete=models.SET_NULL,null=True)
    quiz = models.ForeignKey(Quiz, related_name="quizs", on_delete=models.CASCADE)
    text = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.text
    
    def quiz_show(self):
        max_quiz = self.quiz.count()
        return max_quiz




class Reverso(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    percentage = models.IntegerField(null=True)
    correct = models.IntegerField()
    wrong = models.IntegerField()
    times = models.IntegerField(null=True)
    total = models.IntegerField() 


     # @property
    # def percentage(self):
    #     pass
    def __str__(self):
        return  self.name
    

# class Reversodetail(models.Model):
    




