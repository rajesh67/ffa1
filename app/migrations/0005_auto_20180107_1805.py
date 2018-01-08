# Generated by Django 2.0 on 2018-01-07 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20171221_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('1', 'Medication/Sponse'), ('2', 'Adoption'), ('3', 'Donation'), ('4', 'About US'), ('5', 'Contact US')], max_length=1, unique=True),
        ),
    ]