# Generated by Django 4.1.4 on 2023-01-02 05:18

from django.db import migrations, models
import system.models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesspermit',
            name='mayor_full_name',
            field=models.CharField(default=system.models.get_mayor_full_name, max_length=50),
        ),
        migrations.AlterField(
            model_name='businesspermit',
            name='mayor_signature',
            field=models.ImageField(blank=True, default=system.models.get_mayor_signature, null=True, upload_to='signatures/'),
        ),
        migrations.AlterField(
            model_name='config',
            name='mayor_signature',
            field=models.ImageField(blank=True, default='/media/signatures/signature.png', null=True, upload_to='signatures/'),
        ),
    ]
