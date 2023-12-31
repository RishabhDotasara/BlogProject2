from django.db import models
from django.contrib.auth.models import User

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

#     def __str__(self):
#         return self.name



class Post(models.Model):
    # post_id = models.BigAutoField(verbose_name='id')
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE,default='',null=True)
    title = models.CharField(max_length=255,default="No Title")
    views = models.IntegerField(default=0)
    posted_on = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='images/',default='')
    # author = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,  null=True)

    def __str__(self):
        return self.title
    
    # @property
    # def author_name(self):
    #     return self.author.name
    
    # @property
    # def author_occu(self):
    #     return self.author.occupation
    
    # @property
    # def author_yr(self):
    #     return self.author.clg_yr

class Profile(models.Model):

    occu_choice = (
        ('Student','Student'),
        ('Professor','Professor'),
        ('Worker','Worker')
    )

    yr_choice = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )

    deg_choice = (
        ('B.tech','B.Tech'),
        ('M.Tech','M.Tech'),
        ('Ph.D','Ph.D'),
        ('BS','BS')
    )
    author_real = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    author_name = models.CharField(max_length=255,default='')
    age = models.IntegerField(default=0)
    occupation = models.CharField(max_length=50,choices=occu_choice,default='Student')
    clg_yr = models.IntegerField(choices=yr_choice,default=1)
    deg = models.CharField(max_length=50,choices=deg_choice,default='B.Tech')

    def __str__(self):
        return self.author_name