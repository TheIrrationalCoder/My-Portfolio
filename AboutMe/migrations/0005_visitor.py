# Generated by Django 3.2.25 on 2024-07-05 05:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('AboutMe', '0004_person_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('visitor_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=500)),
                ('linkedinh', models.CharField(max_length=1000)),
            ],
        ),
    ]
