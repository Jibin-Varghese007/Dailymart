# Generated by Django 5.0.3 on 2024-06-11 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0002_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('PhoneNumber', models.IntegerField()),
                ('Productname', models.CharField(max_length=20)),
                ('Productquantity', models.IntegerField()),
                ('Productotal', models.IntegerField()),
            ],
        ),
    ]
