# Generated by Django 4.2.7 on 2023-11-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_offers', '0004_remove_joboffer_employer_joboffer_employer_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='company_name',
            field=models.CharField(default='UnknownCompany', max_length=100),
        ),
    ]