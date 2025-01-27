# Generated by Django 5.0.2 on 2024-03-02 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('django_cron', '0001_initial'), ('django_cron', '0002_remove_max_length_from_CronJobLog_message'), ('django_cron', '0003_cronjoblock'), ('django_cron', '0004_rename_cronjoblog_code_start_time_ran_at_time_django_cron_code_21f381_idx_and_more')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CronJobLock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=200, unique=True)),
                ('locked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CronJobLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=64)),
                ('start_time', models.DateTimeField(db_index=True)),
                ('end_time', models.DateTimeField(db_index=True)),
                ('is_success', models.BooleanField(default=False)),
                ('message', models.TextField(blank=True, default='')),
                ('ran_at_time', models.TimeField(blank=True, db_index=True, editable=False, null=True)),
            ],
            options={
                'indexes': [models.Index(fields=['code', 'start_time', 'ran_at_time'], name='django_cron_code_21f381_idx'), models.Index(fields=['code', 'is_success', 'ran_at_time'], name='django_cron_code_89ad04_idx'), models.Index(fields=['code', 'start_time'], name='django_cron_code_966ed3_idx')],
            },
        ),
    ]
