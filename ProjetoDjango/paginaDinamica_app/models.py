from django.db import models

class Aluno(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    serie = models.CharField(max_length=10)

    def __str__(self):
        return self.name
