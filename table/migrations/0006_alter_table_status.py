# Generated by Django 3.2.5 on 2021-07-22 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0005_merge_0004_auto_20210717_1816_0004_auto_20210717_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.ForeignKey(help_text='choice status for table', on_delete=django.db.models.deletion.CASCADE, to='table.status', verbose_name='status:'),
        ),
    ]
