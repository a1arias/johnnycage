from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=32)
    content = models.TextField()
    title = models.CharField(max_length=200, default='Change Me')
    subtitle = models.CharField(max_length=200, default='What else?')
    slogan = models.CharField(max_length=150, default='Another cool site by adri.codes')
    mainstatement = models.TextField(max_length=400, default='Change me to something crafty or witty')
    readmorebtn = models.CharField(max_length=50, default='Continue Reading&raquo;')
    mainreadmorebtn = models.CharField(max_length=50, default='Read more&raquo;')

    def __str__(self):
        return self.name
