# Generated by Django 4.2.7 on 2023-11-17 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0002_remove_employerprofile_job_offers'),
        ('job_offers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joboffer',
            old_name='expiration_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='publication_date',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='requirements',
        ),
        migrations.AddField(
            model_name='joboffer',
            name='employer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='employers.employerprofile'),
        ),
    ]