# Generated by Django 3.1.7 on 2021-04-01 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intradaymarketdata',
            fields=[
                ('dt', models.DateTimeField(primary_key=True, serialize=False)),
                ('trade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numtrades', models.IntegerField()),
                ('lowtoday', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hightoday', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'intradaymarketdata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Modelfactors',
            fields=[
                ('dt', models.DateTimeField(primary_key=True, serialize=False)),
                ('ret_5_min', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
                ('ret_30_min', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
                ('ret_1_hour', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
                ('ret_3_hour', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
                ('ret_6_hour', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
                ('ret_12_hour', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
                ('ret_24_hour', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
                ('volume_5_min_vnorm', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('volume_30_min_vnorm', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('volume_1_hour_vnorm', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('volume_3_hour_vnorm', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('volume_6_hour_vnorm', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('volume_12_hour_vnorm', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('volume_24_hour_vnorm', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('volatility_1_hour', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('volatility_3_hour', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('volatility_6_hour', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('volatility_12_hour', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('volatility_24_hour', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('avg_trd_size_5_min', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('avg_trd_size_30_min', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('avg_trd_size_1_hour', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('avg_trd_size_3_hour', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('avg_trd_size_6_hour', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('avg_trd_size_12_hour', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('avg_trd_size_24_hour', models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True)),
                ('ret_in_1_hour', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
                ('ret_in_12_hour', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
                ('ret_in_24_hour', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
                ('volume_5_min', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('volume_30_min', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('volume_1_hour', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('volume_3_hour', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('volume_6_hour', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('volume_12_hour', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('volume_24_hour', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
            options={
                'db_table': 'modelfactors',
                'managed': False,
            },
        ),
    ]
