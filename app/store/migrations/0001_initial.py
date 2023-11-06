# Generated by Django 4.2.7 on 2023-11-06 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=50)),
            ],
        ),
    ]