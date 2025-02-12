# Generated by Django 5.1.4 on 2025-02-08 03:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JS_Manage', '0003_remove_banggiavang_giavang_banggiavang_giaban_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='hoaDonMuaLai',
            fields=[
                ('maHD', models.CharField(default='DEFAULT_VALUE', max_length=10, primary_key=True, serialize=False)),
                ('ngayTao', models.DateField()),
                ('tongTien', models.DecimalField(decimal_places=2, max_digits=10)),
                ('maKH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JS_Manage.khachhang')),
                ('maNV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JS_Manage.nhanvien')),
            ],
        ),
    ]
