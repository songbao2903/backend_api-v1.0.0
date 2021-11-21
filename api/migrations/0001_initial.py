# Generated by Django 2.2.10 on 2020-10-09 16:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catelog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('on_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'catelog',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester_id', models.CharField(blank=True, max_length=50)),
                ('customer_name', models.CharField(max_length=200, null=True)),
                ('main_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=200, null=True)),
                ('fax_number', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('on_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('on_confirm', models.BooleanField(default=False)),
                ('on_active', models.BooleanField(default=True)),
                ('signed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('on_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'package',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('price', models.IntegerField(blank=True, default=0)),
                ('to', models.CharField(blank=True, max_length=50)),
                ('src', models.ImageField(blank=True, null=True, upload_to='product_image')),
                ('link', models.CharField(blank=True, max_length=50)),
                ('description_vn', models.TextField(blank=True)),
                ('description_en', models.TextField(blank=True)),
                ('brief_description_vn', models.TextField(blank=True)),
                ('brief_description_en', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('on_active', models.BooleanField(default=True)),
                ('catelog_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Catelog')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='Static',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('hotline', models.CharField(max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contract_name', models.CharField(blank=True, max_length=100, null=True)),
                ('registration_address', models.CharField(blank=True, max_length=100, null=True)),
                ('tranding_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'static',
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('status', models.IntegerField(choices=[('Active', 1), ('Deactive', 0)], default=1, validators=[django.core.validators.MaxLengthValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tenant',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, unique=True)),
                ('priority', models.IntegerField(choices=[('Thấp', 1), ('Trung bình', 2), ('Cao', 3), ('Rất cao', 4)], default=1, validators=[django.core.validators.MaxLengthValidator(5)])),
                ('mobile_number', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('ticket_type', models.IntegerField(choices=[('Hỗ trợ sản phẩm', 1), ('Hỗ trợ từ xa', 2), ('Đặt lịch tương tác', 3)], default=1, validators=[django.core.validators.MaxLengthValidator(5)])),
                ('verify_code', models.CharField(max_length=15, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[('Opened', 1), ('Pending', 2), ('Stuck', 3), ('Closed', 0)], default=1, validators=[django.core.validators.MaxLengthValidator(5)])),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_customer', to='api.Customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_product', to='api.Product')),
                ('tenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_tenant', to='api.Tenant')),
            ],
            options={
                'db_table': 'ticket',
            },
        ),
        migrations.CreateModel(
            name='TicketActionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_status', models.IntegerField(choices=[('Opened', 1), ('Pending', 2), ('Stuck', 3), ('Closed', 0)], default=1, validators=[django.core.validators.MaxLengthValidator(5)])),
                ('status', models.IntegerField(choices=[('Opened', 1), ('Pending', 2), ('Stuck', 3), ('Closed', 0)], default=1, validators=[django.core.validators.MaxLengthValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_log', to='api.Ticket')),
            ],
            options={
                'db_table': 'ticket_action_log',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_id', models.IntegerField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('on_active', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.CreateModel(
            name='ProductOfOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('on_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_of_order', to='api.Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
            ],
            options={
                'db_table': 'product_of_order',
            },
        ),
        migrations.CreateModel(
            name='ProductOfCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_id', models.IntegerField(blank=True, default=None, null=True)),
                ('on_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
            ],
            options={
                'db_table': 'product_of_customer',
            },
        ),
        migrations.CreateModel(
            name='PackageOfProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('on_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Package')),
                ('product_of_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='package_of_product_order', to='api.ProductOfOrder')),
            ],
            options={
                'db_table': 'package_of_product_order',
            },
        ),
        migrations.CreateModel(
            name='PackageOfProductCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('RESTARING', 'RESTARING')], default='ACTIVE', max_length=50)),
                ('view', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('on_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Package')),
                ('product_of_customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='package_of_product_customer', to='api.ProductOfCustomer')),
            ],
            options={
                'db_table': 'package_of_product_customer',
            },
        ),
        migrations.AddField(
            model_name='package',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='package', to='api.Product'),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('view', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contract_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('on_active', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Order')),
            ],
            options={
                'db_table': 'contract',
            },
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=15)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alert_customer', to='api.Customer')),
            ],
            options={
                'db_table': 'alert',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=51, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('fullname', models.CharField(blank=True, default=None, max_length=255)),
                ('account_code', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('identity_card', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('mobile', models.CharField(blank=True, max_length=50)),
                ('fax', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('first_login', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('on_active', models.BooleanField(default=True)),
                ('customer_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Role')),
            ],
            options={
                'db_table': 'account',
            },
        ),
    ]