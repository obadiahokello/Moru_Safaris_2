# Generated by Django 4.2.4 on 2024-02-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moru', '0005_remove_tour_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itinerary_activity', models.CharField(max_length=1000)),
            ],
        ),
    ]
