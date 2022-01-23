# Generated by Django 4.0.1 on 2022-01-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text="A date of author's birth (or Null, if unknown).", null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, help_text="A date of author's death (or Null, if alive or unknown).", null=True),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateField(blank=True, null=True),
        ),
    ]
