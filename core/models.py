from django.db import models

class Cartoon(models.Model):
    name= models.CharField(max_length=31)
    photo= models.CharField(max_length=255)
    about= models.TextField()
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.about