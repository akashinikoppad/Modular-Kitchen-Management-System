# Generated by Django 3.2 on 2021-06-02 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sanjivini_home', '0006_alter_customermodel_designer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installmodel',
            name='payid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanjivini_home.customermodel'),
        ),
    ]
