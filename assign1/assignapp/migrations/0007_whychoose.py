# Generated by Django 4.2.4 on 2023-08-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignapp', '0006_alter_serivieinfo_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='whychoose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]