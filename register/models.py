from django.db import models

class User(models.Model):

    mName = models.CharField(max_length = 20)
    mEmail = models.CharField(max_length = 30, primary_key = True)
    mPhone = models.IntegerField(default = 10)
    mPassword = models.CharField(max_length = 30)

class Message(models.Model):

    mEmail = models.ForeignKey(User, on_delete = models.CASCADE)
    mMsg = models.CharField(max_length = 300)
