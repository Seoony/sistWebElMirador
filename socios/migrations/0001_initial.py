# Generated by Django 4.1.7 on 2023-02-19 05:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('fecha_de_ingreso', models.DateTimeField(default=django.utils.timezone.now)),
                ('nombres', models.CharField(max_length=63)),
                ('primer_apellido', models.CharField(max_length=31)),
                ('segundo_apellido', models.CharField(max_length=31)),
                ('celular', models.CharField(max_length=9, null=True)),
                ('vivencia', models.BooleanField(default=False)),
                ('fecha_de_nacimiento', models.DateField()),
                ('agua', models.BooleanField(default=False)),
                ('luz', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
