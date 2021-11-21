# Generated by Django 2.2.10 on 2020-10-21 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_order_order_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_status', models.BooleanField(default=True)),
                ('payment_time', models.DateTimeField()),
                ('paid', models.IntegerField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('on_active', models.BooleanField(default=True)),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Contract')),
            ],
            options={
                'db_table': 'billing',
            },
        ),
    ]