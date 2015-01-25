from django.contrib import admin

# Register your models here.
from django.contrib import admin
from polls.models import Question
from polls.models import Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text','pub_date','was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    
admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)