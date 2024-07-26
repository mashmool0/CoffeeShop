from django.shortcuts import render
from .models import Food, FoodsField, SectionFood


# Create your views here.

def landing(request):
    food = Food.objects.all()
    food_field = FoodsField.objects.all()
    section_food = SectionFood.objects.all()

    return render(request, 'Landing/index.html',
                  context={"food": food, "food_field": food_field, "section_food": section_food})
