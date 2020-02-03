# Generated by Django 2.2.7 on 2020-02-03 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('byname', models.CharField(max_length=20)),
                ('age', models.IntegerField(null=True)),
                ('breed', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Curators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogshelter.Dogs')),
            ],
        ),
        migrations.CreateModel(
            name='Costs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('treatment', models.CharField(max_length=20)),
                ('veterinarian', models.CharField(max_length=20)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogshelter.Dogs')),
            ],
        ),
    ]
