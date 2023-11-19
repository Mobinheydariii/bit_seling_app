# Generated by Django 4.2.7 on 2023-11-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='تایتل بیت')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ(url)')),
                ('bpm', models.BigIntegerField(verbose_name='')),
                ('keys', models.CharField(max_length=2)),
                ('publish', models.DateField(blank=True, null=True, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='bits/images/image/', verbose_name='تصویر بیت')),
                ('mp3_free', models.FileField(upload_to='bits/files/mp3/free/', verbose_name='mp3 رایگان')),
                ('mp3_no_tag_in', models.FileField(upload_to='bits/files/mp3/no_tag/', verbose_name='pm3 پولی')),
                ('wav', models.FileField(upload_to='bits/files/wav/', verbose_name='فایل wav')),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('َAC', 'Accepted'), ('RJ', 'Rejected')], default='DF', max_length=3)),
                ('plays', models.IntegerField(default=0, verbose_name='تعداد پلی')),
                ('likes', models.IntegerField(default=0, verbose_name='تعداد لایک')),
                ('dislikes', models.IntegerField(default=0, verbose_name='تعداد dislike ها')),
                ('comments', models.IntegerField(default=0, verbose_name='تعداد کامنت ها')),
            ],
            options={
                'verbose_name': 'بیت',
                'verbose_name_plural': 'بیت ها',
                'ordering': ['-publish'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام دسته بندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ دسته بندی')),
                ('image', models.ImageField(upload_to='categories/images/', verbose_name='تصویر دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام برچسب')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ برچسب')),
            ],
            options={
                'verbose_name': 'برچسب',
                'verbose_name_plural': 'برچسب ها',
            },
        ),
    ]