# Generated by Django 3.2.4 on 2021-06-18 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_auto_20210618_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='applyAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Internship', 'Internship'), ('Remotly', 'Remotly')], max_length=50),
        ),
    ]
