# Generated by Django 2.2.3 on 2020-10-29 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20201029_1206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': '地区', 'verbose_name_plural': '地区'},
        ),
        migrations.AlterModelOptions(
            name='copyrightinfo',
            options={'verbose_name': '版权信息管理', 'verbose_name_plural': '版权信息管理'},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'verbose_name': '语言', 'verbose_name_plural': '语言'},
        ),
        migrations.AlterModelOptions(
            name='movieinfo',
            options={'verbose_name': '电影信息', 'verbose_name_plural': '电影信息'},
        ),
        migrations.AlterModelOptions(
            name='orderinfo',
            options={'verbose_name': '订单信息', 'verbose_name_plural': '订单信息'},
        ),
        migrations.AlterModelOptions(
            name='rightinfo',
            options={'verbose_name': '权利信息', 'verbose_name_plural': '权利信息'},
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': '版本', 'verbose_name_plural': '版本'},
        ),
        migrations.AlterField(
            model_name='area',
            name='areaname',
            field=models.CharField(max_length=50, verbose_name='地区名'),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(max_length=50, verbose_name='语言名'),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Area', verbose_name='地区'),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='dubbing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dubbing', to='movies.Language', verbose_name='配音'),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='introduce',
            field=models.TextField(default='还没有任何介绍', verbose_name='电影简介'),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='name',
            field=models.CharField(max_length=255, verbose_name='电影名'),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='subtitle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtitle', to='movies.Language', verbose_name='字幕'),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='time',
            field=models.CharField(max_length=50, verbose_name='时长'),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Version', verbose_name='版本'),
        ),
        migrations.AlterField(
            model_name='version',
            name='versionname',
            field=models.CharField(max_length=50, verbose_name='版本名'),
        ),
    ]
