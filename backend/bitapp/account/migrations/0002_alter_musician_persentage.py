# Generated by Django 4.2.7 on 2023-11-24 05:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='persentage',
            field=models.IntegerField(default=80, help_text='سهم موزیسین از فروش بیت بین 80 تا 100 درصد می باشد', validators=[django.core.validators.MinValueValidator(80), django.core.validators.MaxValueValidator(100)], verbose_name='سهم موزیسین'),
        ),
    ]
