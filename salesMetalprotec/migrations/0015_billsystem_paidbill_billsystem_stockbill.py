# Generated by Django 4.2 on 2023-07-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesMetalprotec', '0014_creditnotesystem_origincreditnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='billsystem',
            name='paidBill',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='billsystem',
            name='stockBill',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]