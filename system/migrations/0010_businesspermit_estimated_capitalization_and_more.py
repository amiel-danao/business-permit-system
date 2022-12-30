# Generated by Django 4.1.4 on 2022-12-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_businesspermit_seating_capacity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesspermit',
            name='estimated_capitalization',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='motorized_tricycle_delivery',
            field=models.CharField(blank=True, default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='motorized_tricycle_peddling',
            field=models.CharField(blank=True, default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='no_of_beds',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='no_of_boarders',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='weight_of_45kgs_delivery',
            field=models.CharField(blank=True, default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='weight_of_45kgs_peddling',
            field=models.CharField(blank=True, default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='weight_of_below_45kgs_delivery',
            field=models.CharField(blank=True, default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='weight_of_below_45kgs_peddling',
            field=models.CharField(blank=True, default='0', max_length=30),
        ),
    ]