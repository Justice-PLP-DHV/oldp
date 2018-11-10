# Generated by Django 2.1.2 on 2018-11-05 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0012_auto_20181025_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='following_cases',
            field=models.ManyToManyField(blank=True, help_text='Cases from superior courts (higher judicial authority)', related_name='_case_following_cases_+', to='cases.Case'),
        ),
        migrations.AddField(
            model_name='case',
            name='following_cases_raw',
            field=models.TextField(blank=True, help_text='Cases from inferior courts as in source HTML', null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='preceding_cases',
            field=models.ManyToManyField(blank=True, help_text='Cases from inferior courts (lower judicial authority)', related_name='_case_preceding_cases_+', to='cases.Case'),
        ),
        migrations.AddField(
            model_name='case',
            name='preceding_cases_raw',
            field=models.TextField(blank=True, help_text='Cases from inferior courts as in source HTML', null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='court_raw',
            field=models.CharField(default='{}', help_text='Raw court information from crawler (JSON)', max_length=255),
        ),
    ]
