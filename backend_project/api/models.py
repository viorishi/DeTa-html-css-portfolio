from django.db import models
from django.contrib.auth.models import User #ProjectSpecific

class Note(models.Model):#ProjectSpecific
    title = models.CharField(max_length=100) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes") # Link data to the user 

    def __str__(self):
        return self.title