# Generated by Django 2.2 on 2019-07-10 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_gii_pcmark', '0023_auto_20190710_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='system',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='django_gii_pcmark.System'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='test_pack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_gii_pcmark.TestPack'),
        ),
    ]
