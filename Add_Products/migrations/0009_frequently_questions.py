# Generated by Django 5.0.2 on 2024-03-08 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Add_Products', '0008_demomodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frequently_Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField()),
                ('Answer', models.TextField()),
            ],
        ),
    ]
