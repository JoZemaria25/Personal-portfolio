from django.db import models
import datetime
class Blog(models.Model):
    New_Blog = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default='SOME STRING')
    date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.New_Blog
