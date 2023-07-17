# Generated by Django 4.2.2 on 2023-07-13 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settingsMetalprotec', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('salesMetalprotec', '0007_rename_endpointguide_billsystem_endpointbill_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='bankSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameBank', models.CharField(blank=True, max_length=12, null=True)),
                ('currencyBank', models.CharField(blank=True, max_length=10, null=True)),
                ('accountNumber', models.CharField(blank=True, max_length=32, null=True)),
                ('moneyBank', models.CharField(blank=True, max_length=12, null=True)),
                ('endpointBank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='settingsMetalprotec.endpointsystem')),
            ],
        ),
        migrations.CreateModel(
            name='paymentSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datePayment', models.DateField(blank=True, null=True)),
                ('nameBankPayment', models.CharField(blank=True, max_length=12, null=True)),
                ('currencyPayment', models.CharField(blank=True, max_length=12, null=True)),
                ('operationNumber', models.CharField(blank=True, max_length=24, null=True)),
                ('nameClient', models.CharField(blank=True, max_length=128, null=True)),
                ('statePayment', models.CharField(blank=True, max_length=12, null=True)),
                ('codeDocument', models.CharField(blank=True, max_length=12, null=True)),
                ('codeGuide', models.CharField(blank=True, max_length=12, null=True)),
                ('codeQuotation', models.CharField(blank=True, max_length=12, null=True)),
                ('codeSeller', models.CharField(blank=True, max_length=12, null=True)),
                ('typeDocumentPayment', models.CharField(blank=True, max_length=12, null=True)),
                ('asociatedBank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='financeMetalprotec.banksystem')),
                ('asociatedBill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='salesMetalprotec.billsystem')),
                ('asociatedInvoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='salesMetalprotec.invoicesystem')),
                ('endpointPayment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settingsMetalprotec.endpointsystem')),
            ],
        ),
        migrations.CreateModel(
            name='bankOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOperation', models.DateField(blank=True, null=True)),
                ('currencyOperation', models.CharField(blank=True, max_length=10, null=True)),
                ('detailOperation', models.CharField(blank=True, max_length=64, null=True)),
                ('moneyOperation', models.CharField(blank=True, max_length=12, null=True)),
                ('numberOperation', models.CharField(blank=True, max_length=16, null=True)),
                ('typeOperation', models.CharField(blank=True, max_length=12, null=True)),
                ('stateOperation', models.CharField(blank=True, max_length=12, null=True)),
                ('nameClient', models.CharField(blank=True, max_length=128, null=True)),
                ('nameSeller', models.CharField(blank=True, max_length=64, null=True)),
                ('codeDocument', models.CharField(blank=True, max_length=12, null=True)),
                ('codeQuotation', models.CharField(blank=True, max_length=12, null=True)),
                ('asociatedBank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financeMetalprotec.banksystem')),
                ('asociatedBill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='salesMetalprotec.billsystem')),
                ('asociatedInvoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='salesMetalprotec.invoicesystem')),
                ('asociatedPayment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='financeMetalprotec.paymentsystem')),
                ('asociatedUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('endpointOperation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settingsMetalprotec.endpointsystem')),
            ],
        ),
    ]