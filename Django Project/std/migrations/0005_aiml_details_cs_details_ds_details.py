# Generated by Django 4.2.2 on 2023-07-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('std', '0004_remove_messeges_roll'),
    ]

    operations = [
        migrations.CreateModel(
            name='aiml_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll', models.CharField(max_length=15, verbose_name='Roll')),
                ('Name', models.CharField(max_length=20, verbose_name='Name')),
                ('Gender', models.CharField(max_length=1, verbose_name='Gender')),
                ('Cou', models.CharField(max_length=4, verbose_name='Cou')),
            ],
        ),
        migrations.CreateModel(
            name='cs_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll', models.CharField(max_length=15, verbose_name='Roll')),
                ('Name', models.CharField(max_length=20, verbose_name='Name')),
                ('Gender', models.CharField(max_length=1, verbose_name='Gender')),
                ('Cou', models.CharField(max_length=4, verbose_name='Cou')),
            ],
        ),
        migrations.CreateModel(
            name='ds_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll', models.CharField(max_length=15, verbose_name='Roll')),
                ('Name', models.CharField(max_length=20, verbose_name='Name')),
                ('Gender', models.CharField(max_length=1, verbose_name='Gender')),
                ('Cou', models.CharField(max_length=4, verbose_name='Cou')),
            ],
        ),
    ]
