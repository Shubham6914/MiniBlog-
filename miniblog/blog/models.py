from django.db import models


# creating table for dashboard using models 

class post(models.Model):
   title = models.CharField(max_length=150)
   description = models.TextField()

