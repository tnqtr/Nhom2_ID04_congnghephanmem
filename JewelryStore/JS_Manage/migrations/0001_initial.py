# Generated by Django 5.1.4 on 2025-01-13 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Cre', models.DateField()),
                ('CustomID', models.CharField(max_length=10)),
                ('StaffID', models.CharField(max_length=10)),
                ('Total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bill_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mount', models.IntegerField()),
                ('Unit_Price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StaffID', models.CharField(max_length=10)),
                ('FName', models.CharField(max_length=100)),
            ],
        ),
    ]
