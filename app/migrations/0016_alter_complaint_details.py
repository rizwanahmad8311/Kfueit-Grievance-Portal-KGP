# Generated by Django 4.1.7 on 2023-05-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_complaint_cancel_at_alter_complaint_closed_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='details',
            field=models.CharField(max_length=2500),
        ),
    ]
