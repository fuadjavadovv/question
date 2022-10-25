from multiprocessing.dummy import Value
from re import I
import re
from turtle import update
from django.shortcuts import render
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.shortcuts import get_object_or_404

from .models import *
from django.http import HttpResponse
 
# Create your views here.
def home(request,id):
    quiz= Quiz.objects.get(id=id)
    questions = Question.objects.all()
    if request.method == 'POST':
        print(request.POST)
        questions=Question.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.text),"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.text):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        # S= Reverso.objects.filter(quiz=id).name
        # print(S)
        form = Reverso.objects.create(quiz=quiz,name=request.POST["fname"],correct=correct,wrong=wrong,percentage=percent,total=total,times=request.POST.get('timer'))
        form.save()
        print(correct ,"fffffffffffffffffffff")
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            
            # 'form':form
        }
      
        return render(request,'result.html',context)
    else:
       
        questions=Question.objects.filter(quiz=id)
        context = {
            'questions':questions,
           
        }
        return render(request,'home.html',context)
 
def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'addquestion.html',context)
    else: 
        return redirect('home') 
   

def updatequestion(request,id):
    question= get_object_or_404(Question,id=id)
    form = UpdateQuestionform(request.POST or None,instance=question)
    if form.is_valid():
        question = form.save(commit=False)
        question.save()
        return redirect('dashboard')
    return render(request,'updatequestion.html',{'form':form})
def addQuiz(request):
    if request.user.is_staff:
        form = addQuizform()
        if request.method == "POST":
            form=addQuizform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        return  render(request,'addquiz.html',{'form':form})
    else:
        return redirect('home')
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect(' ')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')


def testingPage(request):
    quiz = Quiz.objects.all()

 
    return render(request,'testing.html',{'quiz':quiz})

def reversopage(request):
    reversos= Reverso.objects.filter(quiz__user=request.user)
    return render(request,'revorso.html',{'reversos':reversos})

def reversodetail(request):
    
    return render(request,'reversodefault')
def dashboard(request):
    quiz = Quiz.objects.filter(user=request.user)

    return render(request,"dashboard.html",{'quiz':quiz})

def changepage(request,id):
    question = Question.objects.filter(quiz=id)
    return render(request,"change.html",{'question':question})

def deletequestion(request,pk):
     if request.method=="POST":
        question = Question.objects.get(pk=pk)
        question.delete()
     return redirect('dashboard')

