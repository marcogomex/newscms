# Generated by Django 2.2.17 on 2021-01-31 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newscategory_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date', '-id'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]
