# Generated by Django 4.1.3 on 2022-11-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_rename_countryname_country_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='upDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
