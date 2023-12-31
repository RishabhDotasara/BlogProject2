from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.
# class Author(models.Model):
#     occu_choice = (
#         ('Student','Student'),
#         ('Professor','Professor'),
#         ('Worker','Worker')
#     )

#     yr_choice = (
#         (1,1),
#         (2,2),
#         (3,3),
#         (4,4),
#         (5,5)
#     )

#     deg_choice = (
#         ('B.tech','B.Tech'),
#         ('M.Tech','M.Tech'),
#         ('Ph.D','Ph.D'),
#         ('BS','BS')
#     )
#     user
#     name = models.CharField(max_length=255,default='')
#     age = models.IntegerField(default=0)
#     occupation = models.CharField(max_length=255,choices=occu_choice,default='Student')
#     clg_yr = models.IntegerField(default=0)
#     degree = models.CharField(max_length=255,choices=deg_choice,default='B.Tech')


class Profile(models.Model):

    occu_choice = (
        ('Student','Student'),
        ('Professor','Professor'),
        ('Worker','Worker')
    )

    yr_choice = (
        ('First','First'),
        ('Second','Second'),
        ('Third','Third'),
        ('Fourth','Fourth'),
        ('Fifth','Fifth')
    )

    deg_choice = (
        ('B.tech','B.Tech'),
        ('M.Tech','M.Tech'),
        ('Ph.D','Ph.D'),
        ('BS','BS'),
        ('Dual Degree','Dual Degree')
    )
    author_real = models.ForeignKey('auth.user',on_delete=models.CASCADE,null=True,blank=True)
    author_name = models.CharField(max_length=255,default='')
    age = models.IntegerField(default=0)
    occupation = models.CharField(max_length=50,choices=occu_choice,default='Student')
    clg_yr = models.CharField(max_length=25,choices=yr_choice,default='First')
    deg = models.CharField(max_length=50,choices=deg_choice,default='B.Tech')

    def __str__(self):
        return f'{self.author_name} | {self.author_real}'
#     def __str__(self):
#         return self.name

    def is_student(self):
        self.is_stu = bool
        if self.occupation == "Student":
            self.is_stu = True
        else:
            self.is_stu = False
        return self.is_stu

class Post(models.Model):
    post_id = models.IntegerField(default=0,unique=True)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,default='')
    title = models.CharField(max_length=255,default="No Title")
    views = models.IntegerField(default=0)
    posted_on = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/',default='')
    content = RichTextField(default='',blank=True,null=True)
    
    # author = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,  null=True)

    def __str__(self):
        return f'{self.title}'
    
    # @property
    # def author_name(self):
    #     return self.author.name
    
    # @property
    # def author_occu(self):
    #     return self.author.occupation
    
    # @property
    # def author_yr(self):
    #     return self.author.clg_yr