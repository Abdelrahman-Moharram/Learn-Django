# Generated by Django 3.2.4 on 2021-06-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Internship', 'Internship'), ('Part Time', 'Part Time'), ('Remotly', 'Remotly'), ('Full Time', 'Full Time')], max_length=50),
        ),
    ]
