# Generated by Django 2.2 on 2019-06-28 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_gii_pcmark', '0005_auto_20190628_0613'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanChipsetsDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Справочник: чипсеты сетевых карт',
            },
        ),
        migrations.CreateModel(
            name='WifiChipsetDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Справочник: чипсеты wi-fi карт',
            },
        ),
        migrations.CreateModel(
            name='WifiVersionsDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Справочник: версии wi-fi карт',
            },
        ),
        migrations.AddField(
            model_name='motherboard',
            name='lan1_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='lan2_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='usb2_count',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='usb3_count',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='official_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='lan_chipset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_gii_pcmark.LanChipsetsDict'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='wifi_chipset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_gii_pcmark.WifiChipsetDict'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='wifi_versions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_gii_pcmark.WifiVersionsDict'),
        ),
    ]
