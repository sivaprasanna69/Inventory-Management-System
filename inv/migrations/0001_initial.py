# Generated by Django 2.1.7 on 2020-08-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typee', models.CharField(blank=True, max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(default='SOLD', max_length=100)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typee', models.CharField(blank=True, max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(default='SOLD', max_length=100)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typee', models.CharField(blank=True, max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(default='SOLD', max_length=100)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]