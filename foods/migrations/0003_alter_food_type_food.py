# Generated by Django 4.0.6 on 2022-07-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_food_type_food_alter_food_descriptions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('brakefast', 'صبحانه'), ('dinner', 'شام'), ('lunch', 'ناهار'), ('drinks', 'نوشیدنی')], default='شام', max_length=50, verbose_name='نوع غذا'),
        ),
    ]
