from django.contrib import admin
from .models import FoodsField, Food, SectionFood

# Register your models here.
admin.site.register(Food)
admin.site.register(SectionFood)
admin.site.register(FoodsField)
