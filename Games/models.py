from django.db import models

class Game(models.Model):

    name = models.CharField(max_length=100)
    link = models.URLField(null=True)
    description = models.TextField(null=True)
    rating = models.IntegerField(choices=[(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10')],null=True)
    review = models.TextField(null=True)
