# Generated by Django 4.1.3 on 2022-11-09 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_alter_movie_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='films.country'),
        ),
    ]