from django.db import models

# Create your models here.
class taskModel(models.Model):
    task = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task
    