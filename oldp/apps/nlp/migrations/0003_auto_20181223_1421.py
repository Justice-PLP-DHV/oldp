# Generated by Django 2.1.2 on 2018-12-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlp', '0002_auto_20181124_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='type',
            field=models.CharField(choices=[('MONEY', 'Monetary values with currency.'), ('EURO', 'Euro amounts.'), ('PERSON', 'Name of a person or family.'), ('LOCATION', 'Name of geographical or political locations.'), ('ORGANIZATION', 'Any organizational entity.'), ('PERCENT', 'Percentage amounts.')], default='MONEY', max_length=12),
        ),
        migrations.AlterField(
            model_name='entity',
            name='value',
            field=models.BinaryField(),
        ),
    ]