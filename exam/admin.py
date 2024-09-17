from django.contrib import admin
from .models import Student, Group, Exam, Subject, Question, Answer, Variant

# Register your models here.
class StudentInline(admin.TabularInline):
    model = Student
    extra = 1

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [VariantInline]
    list_display = ('name', )

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
    list_display = ('name',)
