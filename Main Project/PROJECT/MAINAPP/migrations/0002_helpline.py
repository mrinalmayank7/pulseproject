# Generated by Django 3.2.5 on 2022-02-28 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Helpline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=400)),
                ('organization', models.TextField(blank=True)),
                ('helpline_number', models.TextField(blank=True)),
                ('organization_details', models.TextField(blank=True)),
            ],
        ),
    ]
