# Generated by Django 4.2.2 on 2023-07-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesMetalprotec', '0013_alter_guidesystem_purposetransportation'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditnotesystem',
            name='originCreditNote',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
