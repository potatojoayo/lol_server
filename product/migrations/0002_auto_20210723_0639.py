# Generated by Django 3.2.4 on 2021-07-23 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
