# Generated by Django 2.2 on 2019-07-02 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_gii_pcmark', '0017_auto_20190630_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='directx_version',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='val_dimension',
        ),
        migrations.AddField(
            model_name='testsoftdict',
            name='dimension',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
