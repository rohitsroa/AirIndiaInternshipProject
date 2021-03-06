# Generated by Django 2.2.2 on 2019-07-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QueryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=50)),
                ('Service', models.CharField(max_length=100)),
                ('Message', models.TextField(max_length=500)),
                ('Date', models.DateTimeField(auto_now=True)),
                ('Status', models.BooleanField()),
                ('Engineer_Name', models.CharField(max_length=50)),
                ('Manager_Name', models.CharField(max_length=50)),
            ],
        ),
    ]
