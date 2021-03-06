# Generated by Django 3.2.4 on 2021-07-20 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('shipment_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='product.color')),
                ('order', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, related_name='ordered_products', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='product.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='product.size')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='orders', to='order.orderstatus'),
        ),
    ]
