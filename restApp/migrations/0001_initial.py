# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyAlertaAwifs',
            fields=[
                ('objectid', models.AutoField(primary_key=True, serialize=False)),
                ('mes', models.CharField(blank=True, null=True, max_length=10)),
                ('ano', models.SmallIntegerField(blank=True, null=True)),
                ('area_km2', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=38)),
                ('dominio', models.CharField(blank=True, null=True, max_length=200)),
                ('tipo', models.CharField(blank=True, null=True, max_length=15)),
                ('uf', models.SmallIntegerField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, null=True, max_length=2)),
                ('data_imagem', models.DateTimeField(blank=True, null=True)),
                ('shape', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('centroide', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('mesid', models.TextField(blank=True, null=True)),
                ('estagio', models.CharField(blank=True, null=True, max_length=50)),
                ('periodo_prodes', models.CharField(blank=True, null=True, max_length=10)),
            ],
            options={
                'db_table': 'ibama"."vw_alerta_awifs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DailyAlertaDeter',
            fields=[
                ('objectid', models.AutoField(primary_key=True, serialize=False)),
                ('mes', models.CharField(blank=True, null=True, max_length=10)),
                ('ano', models.SmallIntegerField(blank=True, null=True)),
                ('area_km2', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=38)),
                ('dominio', models.CharField(blank=True, null=True, max_length=200)),
                ('tipo', models.CharField(blank=True, null=True, max_length=15)),
                ('uf', models.SmallIntegerField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, null=True, max_length=2)),
                ('data_imagem', models.DateTimeField(blank=True, null=True)),
                ('shape', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('centroide', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('mesid', models.TextField(blank=True, null=True)),
                ('estagio', models.CharField(blank=True, null=True, max_length=50)),
                ('periodo_prodes', models.CharField(blank=True, null=True, max_length=10)),
            ],
            options={
                'db_table': 'ibama"."vw_alerta_deter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DailyAlertaDeterQualif',
            fields=[
                ('objectid', models.AutoField(primary_key=True, serialize=False)),
                ('periodo_prodes', models.CharField(blank=True, null=True, max_length=10)),
                ('mes', models.CharField(blank=True, null=True, max_length=10)),
                ('ano', models.SmallIntegerField(blank=True, null=True)),
                ('mes_ano', models.CharField(blank=True, null=True, max_length=6)),
                ('cicatriz_fogo', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('corte_raso_deter', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('degradacao_deter', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('alta', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('leve', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('moderada', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('falso_positivo', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('nao_avaliado', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('deter_total', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('total_avaliado', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('porc_area_avaliada', models.SmallIntegerField(blank=True, null=True)),
                ('mesid', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ibama"."vw_deter_qualificado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DailyAlertaLandsat',
            fields=[
                ('objectid', models.AutoField(primary_key=True, serialize=False)),
                ('mes', models.CharField(blank=True, null=True, max_length=10)),
                ('ano', models.SmallIntegerField(blank=True, null=True)),
                ('area_km2', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=38)),
                ('dominio', models.CharField(blank=True, null=True, max_length=200)),
                ('tipo', models.CharField(blank=True, null=True, max_length=15)),
                ('uf', models.SmallIntegerField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, null=True, max_length=2)),
                ('data_imagem', models.DateTimeField(blank=True, null=True)),
                ('shape', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('centroide', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('mesid', models.TextField(blank=True, null=True)),
                ('estagio', models.CharField(blank=True, null=True, max_length=50)),
                ('periodo_prodes', models.CharField(blank=True, null=True, max_length=10)),
            ],
            options={
                'db_table': 'ibama"."vw_alerta_indicar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PublicAlertaDeter',
            fields=[
                ('objectid', models.AutoField(primary_key=True, serialize=False)),
                ('mes', models.CharField(blank=True, null=True, max_length=10)),
                ('ano', models.SmallIntegerField(blank=True, null=True)),
                ('area_km2', models.DecimalField(blank=True, null=True, decimal_places=8, max_digits=38)),
                ('area_ha', models.DecimalField(blank=True, null=True, decimal_places=8, max_digits=38)),
                ('municipio', models.CharField(blank=True, null=True, max_length=200)),
                ('dominio', models.CharField(blank=True, null=True, max_length=200)),
                ('tipo', models.CharField(blank=True, null=True, max_length=15)),
                ('quinzena', models.CharField(blank=True, null=True, max_length=5)),
                ('id_des', models.CharField(blank=True, null=True, unique=True, max_length=16)),
                ('ai', models.IntegerField(blank=True, null=True)),
                ('tei', models.IntegerField(blank=True, null=True)),
                ('processo', models.CharField(blank=True, null=True, max_length=20)),
                ('url', models.CharField(blank=True, null=True, max_length=200)),
                ('vistoria', models.CharField(blank=True, null=True, max_length=100)),
                ('resp_vistoria', models.CharField(blank=True, null=True, max_length=150)),
                ('longitude', models.CharField(blank=True, null=True, max_length=17)),
                ('latitude', models.CharField(blank=True, null=True, max_length=17)),
                ('uf', models.SmallIntegerField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, null=True, max_length=2)),
                ('obs', models.CharField(blank=True, null=True, max_length=250)),
                ('id_tablet', models.CharField(blank=True, null=True, max_length=10)),
                ('data_vist', models.CharField(blank=True, null=True, max_length=50)),
                ('globalid', models.CharField(blank=True, null=True, max_length=50)),
                ('dado_final', models.CharField(blank=True, null=True, max_length=1)),
                ('estagio', models.CharField(blank=True, null=True, max_length=50)),
                ('data_imagem', models.DateTimeField(blank=True, null=True)),
                ('shape', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('veg_sec', models.CharField(blank=True, null=True, max_length=100)),
                ('periodo_prodes', models.CharField(blank=True, null=True, max_length=10)),
                ('mesid', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ibama"."vw_publica_alerta_deter_por_periodo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PublicAlertaDeterQualif',
            fields=[
                ('objectid', models.AutoField(primary_key=True, serialize=False)),
                ('periodo_prodes', models.CharField(blank=True, null=True, max_length=10)),
                ('mes', models.CharField(blank=True, null=True, max_length=10)),
                ('ano', models.SmallIntegerField(blank=True, null=True)),
                ('mes_ano', models.CharField(blank=True, null=True, max_length=6)),
                ('cicatriz_fogo', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('corte_raso_deter', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('degradacao_deter', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('alta', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('leve', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('moderada', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('falso_positivo', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('nao_avaliado', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('deter_total', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('total_avaliado', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)),
                ('porc_area_avaliada', models.SmallIntegerField(blank=True, null=True)),
                ('mesid', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ibama"."vw_publica_deter_qualificado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaxaNuvens',
            fields=[
                ('objectid', models.AutoField(primary_key=True, serialize=False)),
                ('mes', models.CharField(blank=True, null=True, max_length=10)),
                ('ano', models.SmallIntegerField(blank=True, null=True)),
                ('uf', models.CharField(blank=True, null=True, max_length=2)),
                ('area_km2', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)),
                ('porc_area_km2', models.DecimalField(blank=True, null=True, decimal_places=0, max_digits=2)),
                ('dat_cadastro', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ibama"."taxa_nuvem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaxaNuvensAml',
            fields=[
                ('objectid', models.AutoField(primary_key=True, serialize=False)),
                ('dat_src', models.DateTimeField(blank=True, null=True)),
                ('f_area', models.DecimalField(blank=True, null=True, decimal_places=8, max_digits=38)),
                ('percent', models.DecimalField(blank=True, null=True, decimal_places=8, max_digits=38)),
                ('mes_maiusc', models.TextField(blank=True, null=True)),
                ('ano', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ibama"."vw_taxa_nuvem_aml',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaxaProdes',
            fields=[
                ('ano_prodes', models.CharField(blank=True, max_length=9, primary_key=True, serialize=False)),
                ('ac', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('am', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('ap', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('ma', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('mt', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('pa', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('ro', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('rr', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('to', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
            ],
            options={
                'db_table': 'public"."taxa_prodes',
                'managed': False,
            },
        ),
    ]