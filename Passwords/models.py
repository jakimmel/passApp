from django.db import models

class Password(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=400)
    group = models.ForeignKey('PassGroup')

    def __unicode__(self):
        return u'' + self.username + ": " + self.password


class PassGroup(models.Model):
    name = models.CharField(max_length=40)
    
    def __unicode__(self):
        return u'' + self.name
