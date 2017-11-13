from django.db import models

# Create your models here.
class TodoItem(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    priority = models.CharField(max_length=6, blank=False, default="medium")
    
    def __str__(self): #this functions tells the admin panel in django administration what to display. In this case the name
        status = "D" if self.done else "N"
        return "{0} ({1})".format(self.name, status)
    
    
