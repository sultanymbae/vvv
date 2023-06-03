from django.db import models


class Questionnaire(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'
              '-', '?'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def __str__(self):
        return self.name
