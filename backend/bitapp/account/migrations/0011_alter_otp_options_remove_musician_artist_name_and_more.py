# Generated by Django 4.2.7 on 2023-12-04 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_otp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otp',
            options={'ordering': ['user'], 'verbose_name': 'otp', 'verbose_name_plural': 'otp'},
        ),
        migrations.RemoveField(
            model_name='musician',
            name='artist_name',
        ),
        migrations.RemoveField(
            model_name='musician',
            name='persentage',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='email',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='password',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='password_conf',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='type',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='artist_name',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='persentage',
        ),
        migrations.RemoveField(
            model_name='singer',
            name='artist_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.AddField(
            model_name='otp',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AddField(
            model_name='user',
            name='otp_auth',
            field=models.BooleanField(default=False, verbose_name='احراض'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, null=True, unique=True, verbose_name='نام کاربری'),
        ),
    ]