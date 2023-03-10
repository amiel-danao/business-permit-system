# Generated by Django 4.1.4 on 2023-01-01 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesspermit',
            name='business_permit_fee',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='businesspermit',
            name='processing_fee',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='businesspermit',
            name='sticker_fee',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
