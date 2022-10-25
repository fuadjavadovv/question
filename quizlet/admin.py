from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)
# Register your models here.
from .models import *



class QuestionInline(admin.TabularInline):
    model = Question
    fields = ('quiz',)
    classes = ('collapse',) #droptown
    

class QuestionAdmin(admin.ModelAdmin):
    list_filter = (('quiz',RelatedDropdownFilter),)
    list_display = ('text','quiz')

admin.site.register(Question,QuestionAdmin)


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name','user','how_question')
    inlines = (QuestionInline,)

admin.site.register(Quiz,QuizAdmin)


class ReversoAdmin(admin.ModelAdmin):
    list_filter = (('percentage',DropdownFilter),)
    list_display = ('quiz','name','percentage')
    search_fields = ['quiz__name',]

admin.site.register(Reverso,ReversoAdmin)