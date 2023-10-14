# Generated by Django 4.2.6 on 2023-10-13 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at')),
                ('suitable_time', models.TimeField(verbose_name='suitable time for contact')),
                ('company_name', models.CharField(max_length=50, verbose_name='company name')),
                ('work_field', models.CharField(max_length=50, verbose_name='work field')),
                ('problem_type', models.CharField(max_length=50, verbose_name='problem type')),
                ('message', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='created by')),
            ],
        ),
    ]
