# Generated by Django 4.0.3 on 2022-03-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='electricity',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='exploration_days',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='explorers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='food',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='humans_alive',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='hunters',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='material_x',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='miners',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='shelter',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='shelter_makers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='solar_panel_cleaner',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='solar_panels',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='steel',
            field=models.IntegerField(default=65),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='water',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='water_gatherers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='weapon_makers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='weapons',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
