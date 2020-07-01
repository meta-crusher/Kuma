from django.db import models

class User(models.Model):

    mName = models.CharField(max_length = 20)
    mUsername = models.CharField(max_length = 20, primary_key=True)
    mEmail = models.CharField(max_length = 30)
    mPhone = models.CharField(max_length = 10)
    mPassword = models.CharField(max_length = 30)

