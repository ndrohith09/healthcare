# Generated by Django 3.1.1 on 2020-11-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_auto_20201107_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='medication',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='problem',
            field=models.TextField(null=True),
        ),
    ]
