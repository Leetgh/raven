# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('reference_number', models.CharField(max_length=50, unique=True)),
                ('investigators_name', models.CharField(max_length=50)),
                ('examiners_name', models.CharField(max_length=50)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ntuser_Lastvisitedmru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=300)),
                ('value', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Ntuser_Mounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.DateField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Ntuser_RecentDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.DateField(max_length=200)),
                ('key_name', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Ntuser_Runkeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=200)),
                ('mruorder', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Ntuser_Runmru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=200)),
                ('mruorder', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Ntuser_SysteminternalsTools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('key_name', models.CharField(max_length=300)),
                ('last_write', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Ntuser_TypedPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Ntuser_TypedUrls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('url_name', models.CharField(max_length=200)),
                ('hive_name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Ntuser_WordWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Software_Activesetup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('key_name', models.CharField(max_length=200)),
                ('stub_path', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Software_APPINIT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=200)),
                ('loadapp_data', models.CharField(max_length=200)),
                ('appinit_data', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Software_BHOS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.DateField()),
                ('value', models.CharField(max_length=200)),
                ('inproc_lastwrite', models.DateField()),
                ('appinit_data', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Software_Runkeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.DateField()),
                ('key_name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Software_Sysinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.DateField()),
                ('os_info', models.CharField(max_length=200)),
                ('installed_date', models.DateField()),
                ('registered_owner', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Software_Userassit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.DateField()),
                ('sub_key', models.CharField(max_length=200)),
                ('runcount', models.DateField()),
                ('windate', models.DateField()),
                ('data', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Software_Winlogon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.DateField()),
                ('key_name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='System_Knowndlls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='System_Mounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='System_Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('key_name', models.CharField(max_length=200)),
                ('impage_path', models.CharField(max_length=200)),
                ('type_name', models.CharField(max_length=200)),
                ('display_name', models.CharField(max_length=200)),
                ('start_type', models.CharField(max_length=200)),
                ('service_dll', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='System_Sysinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('os_info', models.CharField(max_length=200)),
                ('installed_date', models.CharField(max_length=200)),
                ('registered_owner', models.CharField(max_length=200)),
                ('unique_sn', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='System_Terminal_server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('key_name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='System_Usbstor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive', models.CharField(max_length=200)),
                ('last_write', models.CharField(max_length=200)),
                ('key', models.CharField(max_length=200)),
                ('friendly_name', models.CharField(max_length=200)),
                ('unique_sn_lastwrite', models.CharField(max_length=200)),
                ('unique_sn', models.CharField(max_length=200)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registryApp.Case')),
            ],
        ),
    ]
