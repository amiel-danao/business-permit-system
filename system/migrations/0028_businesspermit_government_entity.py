# Generated by Django 4.1.4 on 2022-12-29 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0027_businesspermit_barangay_business_clearance_verified_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesspermit',
            name='government_entity',
            field=models.BooleanField(default=False),
        ),
    ]
