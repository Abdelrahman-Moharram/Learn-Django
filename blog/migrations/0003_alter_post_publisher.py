# Generated by Django 3.2.4 on 2021-06-26 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_usertips_usertype'),
        ('blog', '0002_auto_20210626_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.usertips'),
        ),
    ]
