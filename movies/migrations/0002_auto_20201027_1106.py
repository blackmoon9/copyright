# Generated by Django 2.2.3 on 2020-10-27 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieinfo',
            name='language',
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='dubbing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dubbing', to='movies.Language'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='subtitle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtitle', to='movies.Language'),
        ),
    ]
