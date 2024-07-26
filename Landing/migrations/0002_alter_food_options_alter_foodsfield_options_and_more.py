# Generated by Django 5.0.7 on 2024-07-25 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name': 'خوردنی', 'verbose_name_plural': 'خوردنی ها '},
        ),
        migrations.AlterModelOptions(
            name='foodsfield',
            options={'verbose_name': 'نوع خوردنی', 'verbose_name_plural': 'انواع خوردنی'},
        ),
        migrations.AlterModelOptions(
            name='sectionfood',
            options={'verbose_name': 'طبقه بندی نوع خوردنی', 'verbose_name_plural': 'طبقه بندی انواع خوردنی'},
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.IntegerField(help_text='لطفا قیمت را به شکل تومان وارد کنید مثلا ۹۰'),
        ),
        migrations.AlterField(
            model_name='sectionfood',
            name='foods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_food', to='Landing.foodsfield'),
        ),
    ]