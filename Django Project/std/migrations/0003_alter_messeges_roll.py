# Generated by Django 4.2.1 on 2023-06-29 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('std', '0002_alter_details_cou_alter_details_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messeges',
            name='roll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='std.details'),
        ),
    ]
