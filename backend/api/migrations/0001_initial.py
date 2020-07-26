# Generated by Django 3.0.3 on 2020-07-26 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('holding_number', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100)),
                ('id_number', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Individual')),
            ],
        ),
        migrations.CreateModel(
            name='MedicationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(choices=[('S', 'Sheep'), ('C', 'Cow')], max_length=100)),
                ('species', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_administered', models.FloatField()),
                ('date_of_administration', models.DateField()),
                ('individual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Individual')),
                ('medication_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MedicationType')),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('individuals', models.ManyToManyField(to='api.Individual')),
            ],
        ),
    ]
