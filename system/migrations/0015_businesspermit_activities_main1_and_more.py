# Generated by Django 4.1.4 on 2022-12-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0014_businesspermit_inspection_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesspermit',
            name='activities_main1',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='activities_main2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='activities_main3',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='activities_main4',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='activities_others1',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='activities_others2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='activities_others3',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='activities_others4',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='no_of_units1',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='no_of_units2',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='no_of_units3',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='no_of_units4',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='taxable_items1',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='taxable_items2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='taxable_items3',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='businesspermit',
            name='taxable_items4',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]