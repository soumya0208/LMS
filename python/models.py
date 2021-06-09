from django.db import models
from .validator import file_size
# Create your models here.
class user(models.Model):
    u_name=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    pwd=models.CharField(max_length=50)
    roles=models.CharField(max_length=50)
    ph = models.CharField(max_length=50)
    class Meta:
        db_table="user"
    def __str__(self):
        return self.name+"|"+self.email+"|"+self.pwd+"|"+self.roles+"|"+self.ph+"|"+self.u_name
class doubt(models.Model):
    tu_name=models.CharField(max_length=50)
    coursecode=models.CharField(max_length=50,null=True)
    caption=models.CharField(max_length=50,null=True)
    email=models.EmailField()
    su_name=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    class Meta:
        db_table="doubt"  
class teacher(models.Model):
    u_name=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    coursename=models.CharField(max_length=50)
    coursecode=models.CharField(max_length=50)
    subject= models.CharField(max_length=50)
    minq=models.CharField(max_length=50)
    class Meta:
        db_table="teacher"
    def __str__(self):
        return self.name+"|"+self.coursecode
class videoentry(models.Model):
    u_name=models.CharField(max_length=50)
    coursecode=models.CharField(max_length=50)
    caption=models.CharField(max_length=50,null=True)
    video=models.FileField(upload_to="",null=True)
    class Meta:
        db_table="videoentry"
class student(models.Model):
    tu_name=models.CharField(max_length=50)
    su_name=models.CharField(max_length=50)
    email=models.EmailField()
    name=models.CharField(max_length=50)
    coursecode=models.CharField(max_length=50)
    class Meta:
        db_table="student"
    def __str__(self):
        return self.name+"|"+self.coursecode