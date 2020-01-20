# Generated by Django 2.2.7 on 2020-01-15 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=16, unique=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('c_time', models.DateTimeField(auto_now=True)),
                ('has_confirmed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='login.User')),
                ('head_img', models.ImageField(upload_to='head_img', verbose_name='头像')),
                ('article_num', models.PositiveIntegerField()),
                ('info', models.CharField(max_length=128)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
            ],
            bases=('login.user',),
        ),
        migrations.CreateModel(
            name='UserTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ManyToManyField(related_name='UserTag', related_query_name='UserTag', to='login.User')),
            ],
        ),
        migrations.CreateModel(
            name='Fans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fans', models.ManyToManyField(related_name='fans', related_query_name='fans', to='login.User')),
            ],
        ),
        migrations.CreateModel(
            name='ConfirmString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('c_time', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
            options={
                'verbose_name': '确认码',
                'verbose_name_plural': '确认码',
                'ordering': ['-c_time'],
            },
        ),
    ]