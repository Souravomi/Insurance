# Generated by Django 3.0.8 on 2021-03-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='Balance_Amount',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='Scheme_Amount',
            field=models.CharField(max_length=50),
        ),
    ]
