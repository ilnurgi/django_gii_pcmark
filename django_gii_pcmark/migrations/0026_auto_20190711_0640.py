# Generated by Django 2.2 on 2019-07-11 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_gii_pcmark', '0025_auto_20190710_0653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='gpu_driver',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='os',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='overclock_cpu_freq',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='overclock_gpu_core_freq',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='overclock_gpu_ram_freq',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='overclock_ram_freq',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='screen_size',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='system',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='url',
        ),
    ]