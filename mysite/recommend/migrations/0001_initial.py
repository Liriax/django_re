# Generated by Django 4.0 on 2021-12-23 04:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dora_kpi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('max_value', models.FloatField()),
                ('min_value', models.FloatField(default=0)),
                ('medium_threshold_value', models.FloatField()),
                ('high_threshold_value', models.FloatField()),
                ('elite_threshold_value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('max_value', models.FloatField()),
                ('min_value', models.FloatField(default=0)),
                ('medium_threshold_value', models.FloatField()),
                ('high_threshold_value', models.FloatField()),
                ('elite_threshold_value', models.FloatField()),
                ('low_level', models.BooleanField(default=False)),
                ('source', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('weight', models.FloatField(default=1)),
                ('active', models.BooleanField(default=True)),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='recommend.metric')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('contact_person', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='SuggestedRecommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('suggested', 'SUGGESTED'), ('implemented', 'IMPLEMENTED'), ('rejected', 'REJECTED')], default='suggested', max_length=20)),
                ('confidence', models.FloatField()),
                ('updated_at', models.DateTimeField()),
                ('feedback', models.TextField()),
                ('score', models.IntegerField(choices=[(1, 'Terrible'), (2, 'Bad'), (3, 'Ok'), (4, 'Good'), (5, 'Helpful')])),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='recommend.recommendation')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='recommend.team')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Correlation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=1)),
                ('dora_kpi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correlated_metrics', to='recommend.dora_kpi')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correlated_dora_kpis', to='recommend.metric')),
            ],
            options={
                'unique_together': {('dora_kpi', 'metric')},
            },
        ),
    ]
