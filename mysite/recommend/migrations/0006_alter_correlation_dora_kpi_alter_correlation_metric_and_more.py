# Generated by Django 4.0 on 2021-12-22 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0005_correlation_dora_kpi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correlation',
            name='dora_kpi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correlated_metrics', to='recommend.dora_kpi'),
        ),
        migrations.AlterField(
            model_name='correlation',
            name='metric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correlated_dora_kpis', to='recommend.metric'),
        ),
        migrations.AlterUniqueTogether(
            name='correlation',
            unique_together={('dora_kpi', 'metric')},
        ),
    ]