# Generated by Django 4.0.5 on 2022-08-08 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0003_rename_contact1_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='Contact1',
        ),
    ]