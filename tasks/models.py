from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True) #blank es para que sea opcional en el admin, no para la base de datos
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#con esto se ve el titulo del task desde el administrador y no object
    def __str__(self):
        return self.title + ' - by ' + self.user.username
