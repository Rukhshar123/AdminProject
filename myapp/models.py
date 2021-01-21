from django.db import models
from datetime import date



class User(models.Model):
    username=models.CharField('User Name', max_length=100)
    email=models.CharField('User Email', max_length=100)
    password=models.CharField('User Password', max_length=20)

class Blog(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField('Blog Title',max_length=100)
    description  = models.TextField('PostBlog')
    posted_date = models.DateField(default=date.today)
    name = models.CharField(max_length=50)


class Comment(models.Model):
    message = models.TextField('Message')
    date_comment=models.DateField(default=date.today())
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    post_id= models.ForeignKey(Blog,on_delete=models.CASCADE)