# Generated by Django 2.2.1 on 2019-05-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operator_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataentry',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
