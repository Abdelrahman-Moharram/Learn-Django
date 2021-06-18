# Generated by Django 3.2.4 on 2021-06-18 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_alter_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Remotly', 'Remotly'), ('Internship', 'Internship'), ('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=50),
        ),
    ]
