# Generated by Django 2.0 on 2017-12-20 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171221_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('1', 'Adoption'), ('2', 'Donation'), ('3', 'Medication/Sponse')], max_length=1, unique=True),
        ),
    ]
