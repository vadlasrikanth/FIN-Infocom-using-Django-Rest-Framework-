# Generated by Django 4.1.5 on 2023-02-04 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workexp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.TextField()),
                ('fromdate', models.TextField()),
                ('todate', models.TextField()),
                ('address', models.TextField()),
                ('emp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workExperience', to='Employee_App.employee')),
            ],
        ),
    ]
