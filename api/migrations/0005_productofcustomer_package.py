# Generated by Django 2.2.10 on 2020-10-12 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201012_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='productofcustomer',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Package'),
        ),
    ]