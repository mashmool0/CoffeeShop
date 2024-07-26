from django.db import models


# Create your models here.


class FoodsField(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SectionFood(models.Model):
    foods = models.ForeignKey(FoodsField, on_delete=models.CASCADE, related_name='section_food')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Food(models.Model):
    section_food = models.ForeignKey(SectionFood, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField(help_text="لطفا قیمت را به شکل تومان وارد کنید مثلا ۹۰")

    def __str__(self):
        return self.name + "  " + str(self.price) + " toman"
