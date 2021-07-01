from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    title=models.CharField('Название', max_length=51)
    text=models.TextField('Описание', default='Описание задачи', max_length=255)
    status=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'