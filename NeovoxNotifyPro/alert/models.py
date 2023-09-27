from django.db import models

class Full(models.Model):
    alertname_key = models.CharField(max_length=255)  
    state_key = models.CharField(max_length=255)  
    server = models.CharField(max_length=255)  
    description_key = models.TextField() 
    active_at = models.DateTimeField()
