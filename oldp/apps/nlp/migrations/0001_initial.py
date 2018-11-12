# Generated by Django 2.1.2 on 2018-11-10 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('pos_start', models.IntegerField(null=True)),
                ('pos_end', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NLPContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='entity',
            name='nlp_content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nlp.NLPContent'),
        ),
    ]