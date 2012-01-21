from django.db import models

class Request(models.Model):
    json = models.CharField(max_length=2500)
    
    def __unicode__(self):
        return self.uid.username
