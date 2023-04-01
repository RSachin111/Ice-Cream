# Generated by Django 4.0.5 on 2022-08-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.EmailField(max_length=100)),
                ('subject', models.TextField(max_length=200)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='client',
        ),
    ]