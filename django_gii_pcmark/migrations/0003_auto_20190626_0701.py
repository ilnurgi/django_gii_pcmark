# Generated by Django 2.2 on 2019-06-26 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_gii_pcmark', '0002_auto_20190626_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocard',
            name='max_power',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='max_power', to='django_gii_pcmark.PowersDict'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='min_power',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='min_power', to='django_gii_pcmark.PowersDict'),
        ),
    ]
