from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
    ball = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(max_length=100)
    exam_time = models.DateTimeField()
    # ball = models.PositiveIntegerField()
    subject = models.OneToOneField('Subject', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name} {self.exam_time}'

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.CharField(max_length=100)
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
    answer = models.OneToOneField('Answer', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Answer(models.Model):
    name = models.CharField(max_length=100)
    # question = models.OneToOneField('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Variant(models.Model):
    name = models.CharField(max_length=100)
    questions = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.name