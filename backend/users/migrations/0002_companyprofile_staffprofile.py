# Generated by Django 5.1.6 on 2025-02-22 18:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state_or_region', models.CharField(max_length=255)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(max_length=255)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('contact_person_phone_number', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_profiles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'company_profile',
            },
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255)),
                ('department', models.CharField(choices=[('Applied Biology Program', 'Applied Biology Program'), ('Applied Chemistry', 'Applied Chemistry'), ('Applied Physics', 'Applied Physics'), ('Applied Geology', 'Applied Geology'), ('Applied Mathematics', 'Applied Mathematics'), ('Industrial Chemistry', 'Industrial Chemistry'), ('Pharmacy Program', 'Pharmacy Program'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Electronics & Communication Engineering', 'Electronics & Communication Engineering'), ('Electrical Power and Control Engineering', 'Electrical Power and Control Engineering'), ('Software Engineering', 'Software Engineering'), ('Architecture', 'Architecture'), ('Civil Engineering', 'Civil Engineering'), ('Water Resources Engineering', 'Water Resources Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Material Science and Engineering', 'Material Science and Engineering'), ('Mechanical Engineering', 'Mechanical Engineering')], default=None, max_length=50)),
                ('qualifications', models.CharField(choices=[('Bachelor', 'Bachelor'), ('Master', 'Master'), ('Doctorate', 'Doctorate'), ('Bachelor_Doctorate', 'Both Bachelor and Doctorate'), ('All', 'All (Bachelor, Master, Doctorate)'), ('Doctorate_Master', 'Doctorate and Master')], max_length=50)),
                ('years_of_experience', models.IntegerField()),
                ('expertise', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'staff_profile',
            },
        ),
    ]
