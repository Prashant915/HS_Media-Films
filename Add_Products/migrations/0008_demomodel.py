# Generated by Django 5.0.2 on 2024-02-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Add_Products', '0007_delete_demomodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
