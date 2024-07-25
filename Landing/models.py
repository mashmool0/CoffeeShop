from django.db import models


# Create your models here.


class FoodsField(models.Model):
    name = models.CharField(max_length=50)


class SectionFood(models.Model):
    foods = models.ForeignKey(FoodsField, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Food(models.Model):
    section_food = models.ForeignKey(SectionFood, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
