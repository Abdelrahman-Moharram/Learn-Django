# Generated by Django 3.2.4 on 2021-06-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Remotly', 'Remotly'), ('Internship', 'Internship'), ('Part Time', 'Part Time'), ('Full Time', 'Full Time')], max_length=50),
        ),
    ]
