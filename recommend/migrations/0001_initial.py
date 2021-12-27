# Generated by Django 4.0 on 2021-12-27 03:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dora_kpi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('max_value', models.FloatField(blank=True, null=True)),
                ('min_value', models.FloatField(blank=True, default=0, null=True)),
                ('medium_threshold_value', models.FloatField(blank=True, null=True)),
                ('high_threshold_value', models.FloatField(blank=True, null=True)),
                ('elite_threshold_value', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('max_value', models.FloatField(blank=True, default=1, null=True)),
                ('min_value', models.FloatField(blank=True, default=0, null=True)),
                ('medium_threshold_value', models.FloatField(blank=True, null=True)),
                ('high_threshold_value', models.FloatField(blank=True, null=True)),
                ('elite_threshold_value', models.FloatField(blank=True, null=True)),
                ('low_level', models.BooleanField(default=False)),
                ('source', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('encoded_id', models.IntegerField(primary_key=True, serialize=False)),
                ('headline', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
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
                ('contact_person', models.CharField(blank=True, max_length=250)),
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
                ('confidence', models.FloatField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('feedback', models.TextField(blank=True)),
                ('score', models.IntegerField(blank=True, choices=[(1, 'Terrible'), (2, 'Bad'), (3, 'Ok'), (4, 'Good'), (5, 'Helpful')], null=True)),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='recommend.recommendation')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='recommend.team')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measured_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('object_id', models.PositiveIntegerField()),
                ('value', models.FloatField()),
                ('content_type', models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'recommend'), ('model', 'dora_kpi')), models.Q(('app_label', 'recommend'), ('model', 'metric')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metric_history', to='recommend.team')),
            ],
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
