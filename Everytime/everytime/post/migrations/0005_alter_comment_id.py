# Generated by Django 5.0.3 on 2024-05-30 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_like_post_like_scrap_post_scrap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]