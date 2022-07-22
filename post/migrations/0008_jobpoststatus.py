# Generated by Django 4.0.6 on 2022-07-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_jobpostactivity_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPostStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, verbose_name='채용진행상황')),
            ],
            options={
                'db_table': 'job_post_status',
            },
        ),
    ]
