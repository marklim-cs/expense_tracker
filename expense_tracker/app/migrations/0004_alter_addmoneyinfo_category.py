# Generated by Django 5.1.2 on 2024-11-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_add_money_addmoneyinfo_expense_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmoneyinfo',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Travel', 'Travel'), ('Shopping', 'Shopping'), ('Necessities', 'Necessities'), ('Entertainment', 'Entertainment'), ('Savings', 'Savings'), ('Other', 'Other')], default='Food', max_length=20),
        ),
    ]
