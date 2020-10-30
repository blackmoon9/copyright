# Generated by Django 2.2.3 on 2020-10-29 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0004_auto_20201027_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='RightInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('bankruptcy', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Orderinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('paystyle', models.CharField(max_length=255)),
                ('sellid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selluser', to=settings.AUTH_USER_MODEL)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CopyRightinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('star_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('warning', models.BooleanField()),
                ('warning_time', models.IntegerField()),
                ('remark', models.CharField(max_length=255)),
                ('chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.CopyRightinfo')),
                ('movies_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.MovieInfo')),
                ('oder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Orderinfo')),
                ('right', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.RightInfo')),
            ],
        ),
    ]
