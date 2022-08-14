# Generated by Django 4.0.6 on 2022-07-05 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='')),
                ('descriptions', models.CharField(max_length=50, verbose_name='')),
                ('price', models.IntegerField(verbose_name='')),
                ('time', models.TimeField(verbose_name='')),
                ('pubdate', models.DateField(verbose_name='')),
                ('photo', models.ImageField(upload_to='foods/', verbose_name='')),
            ],
        ),
    ]