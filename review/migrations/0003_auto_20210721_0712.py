# Generated by Django 3.2.4 on 2021-07-21 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='review',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='review.review'),
        ),
        migrations.AlterField(
            model_name='reviewcomment',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='review.review'),
        ),
    ]
