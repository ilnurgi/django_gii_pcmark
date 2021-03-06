# Generated by Django 2.2 on 2019-06-30 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_gii_pcmark', '0012_auto_20190630_0706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpu',
            name='official_url',
        ),
        migrations.AddField(
            model_name='cpu',
            name='max_power',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cpu_max_power', to='django_gii_pcmark.PowersDict'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='min_power',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cpu_min_power', to='django_gii_pcmark.PowersDict'),
        ),
    ]
