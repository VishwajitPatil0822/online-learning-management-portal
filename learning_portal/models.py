from django.db import models
from django.contrib.auth.hashers import make_password

class Contact_Us(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Create_Account(models.Model):
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.BigIntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.id:
            self.password = make_password(self.password)
        super(Create_Account, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Courses(models.Model):
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=100)
    one_line_description = models.CharField(max_length=100, null=True, blank=True)
    full_description = models.CharField(max_length=3000, null=True, blank=True)
    video = models.FileField(upload_to="video/")
    language = models.ForeignKey('Languages', on_delete=models.CASCADE)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Languages(models.Model):
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.language


class Categories(models.Model):
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Quiz(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    course = models.ForeignKey('Courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Certificate(models.Model):
    name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    certificate = models.ImageField(upload_to='certificates/', null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}_{self.course_name}_Certificate"


class My_Learning(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey('Courses', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}___{self.course}"