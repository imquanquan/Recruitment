# Generated by Django 3.1.5 on 2021-02-20 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobhunter',
            name='collect_jobs',
            field=models.ManyToManyField(related_name='collect_set', through='backend.CollectJob', to='backend.Job'),
        ),
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliver_date', models.DateTimeField(auto_now_add=True)),
                ('job_hunter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.jobhunter')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliver_job_set', to='backend.job')),
                ('resume_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.resume')),
            ],
        ),
        migrations.AddField(
            model_name='jobhunter',
            name='deliver_jobs',
            field=models.ManyToManyField(related_name='deliver_set', through='backend.Deliver', to='backend.Job'),
        ),
    ]
