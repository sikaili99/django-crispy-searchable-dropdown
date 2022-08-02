from django.db import models

choices = [('1','BMW'), ('2', 'TOYOTA'),('3', 'TATA'),('4', 'NISAN'),('5', 'LAR')]

class Car(models.Model):
   
    car_type = models.CharField(max_length=24, choices=choices, default='some_y')

    def __str__(self):
        return self.car_type
