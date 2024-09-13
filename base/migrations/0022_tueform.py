# Generated by Django 3.0.5 on 2022-08-11 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0021_sts_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='TueForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='none', max_length=7, null=True)),
                ('sport', models.CharField(max_length=10)),
                ('id_type', models.CharField(max_length=10)),
                ('id_no', models.CharField(max_length=10)),
                ('name_on_id', models.CharField(max_length=10)),
                ('addType', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
                ('district', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('postal_code', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]