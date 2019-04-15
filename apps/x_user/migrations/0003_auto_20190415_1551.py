# Generated by Django 2.0 on 2019-04-15 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('x_team', '0001_initial'),
        ('x_user', '0002_auto_20190415_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='user_team_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_team121', to='x_team.Team_Profile'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_password',
            field=models.CharField(max_length=50, verbose_name='密码'),
        ),
    ]
