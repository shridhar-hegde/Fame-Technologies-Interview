# Generated by Django 2.0.6 on 2018-10-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181013_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='employeeBarcode',
            field=models.ImageField(blank=True, default=True, upload_to='users/'),
            preserve_default=False,
        ),
    ]
