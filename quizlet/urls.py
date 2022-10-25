from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
# from Quiz.views import *
from .views import *
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('', testingPage,name='testing'),
    path('home/<int:id>',home,name='quiz_detail'),
    path('addQuestion/', addQuestion,name='addQuestion'),
    path('dashboard/', dashboard,name='dashboard'),
    path('reverso/', reversopage,name='reverso'),
    path('change/<int:id>',changepage,name='changepage'),
    path('dashboard/<int:pk>',deletequestion,name='deletequestion'),
    path('dashboard/update/<int:id>',updatequestion,name='updatequestion'),
    path('addQuiz/',addQuiz,name='addQuiz'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),

 
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
