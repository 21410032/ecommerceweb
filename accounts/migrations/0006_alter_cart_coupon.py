# Generated by Django 3.2.19 on 2023-07-10 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_coupon_is_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coupon', to='accounts.coupon'),
        ),
    ]
