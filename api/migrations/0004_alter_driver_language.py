# Generated by Django 4.1.7 on 2023-03-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_driver_email_alter_driver_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='language',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]