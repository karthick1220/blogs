# Create your models here
# from django.db import models
# 
# class Home(models.Model):
#     hid = models.CharField(max_length=20)
#     hname = models.CharField(max_length=20)
#     
#     def __str__(self):
#         return self.sname
#     
#     
# class Student(models.Model):
#     sid = models.CharField(max_length=20)
#     sname=models.CharField(max_length=20)
#     hid = models.ForeignKey(Home,on_delete=models.CASCADE)
#     
#     def __str__(self):
#         return self.sname
from django.db import models 

class Reporter(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30) 
    email = models.EmailField()
    
    def __str__(self):
        return "%s%s" % (self.first_name,self.last_name) 
    
class Article(models.Model):
    headline = models.CharField(max_length = 100)
    pub_date = models.DateField() 
    reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline
    
    class Meta:
        ordering = ('headline',)

    
