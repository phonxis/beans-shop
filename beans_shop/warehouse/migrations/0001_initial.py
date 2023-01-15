# Generated by Django 4.0.8 on 2023-01-15 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('weight', models.CharField(blank=True, choices=[('100gram', '100 g'), ('250gram', '250 g'), ('1kg', '1 kg'), ('2kg', '2 kg')], max_length=64, verbose_name='Weight')),
                ('count', models.IntegerField(default=0, verbose_name='Count')),
                ('expiration_dt', models.DateField(verbose_name='Expiration date')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='Creating date')),
                ('updated_dt', models.DateTimeField(auto_now=True, verbose_name='Updating date')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='WarehouseSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_expiration_days', models.IntegerField(default=20, verbose_name='Expiration notification (days)')),
            ],
            options={
                'verbose_name': 'Warehouse settings',
                'verbose_name_plural': 'Warehouse settings',
            },
        ),
        migrations.CreateModel(
            name='ProductAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('sell', 'Sell'), ('cancel_order', 'Cancel Order'), ('restock', 'Restock Beans&Dots'), ('waste', 'Waste (expired product)')], max_length=128, verbose_name='Action')),
                ('previous_count', models.IntegerField(verbose_name='Previous count')),
                ('new_count', models.IntegerField(verbose_name='New count')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='Creating date')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='warehouse.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_actions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product Action',
                'verbose_name_plural': 'Product Actions',
            },
        ),
    ]
