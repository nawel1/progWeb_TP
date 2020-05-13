# Generated by Django 3.0.4 on 2020-04-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('author', models.CharField(blank=True, max_length=256, null=True)),
                ('year', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('price', models.FloatField(blank=True, default=1.0, null=True)),
                ('description', models.TextField(blank=True, max_length=512, null=True)),
                ('bestseller', models.BooleanField(default=False)),
            ],
        ),
    ]