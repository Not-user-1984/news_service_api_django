# Generated by Django 4.2.2 on 2023-06-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_role_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('user', 'Пользователь')], default='user', help_text='Роль пользователя', max_length=50, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Электронная почта пользователя', max_length=254, unique=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(help_text='Имя пользователя', max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(help_text='Фамилия пользователя', max_length=150, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Логин пользователя', max_length=150, unique=True, verbose_name='Логин'),
        ),
    ]
