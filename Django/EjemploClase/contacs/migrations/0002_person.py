# Generated by Django 5.1.2 on 2024-11-02 20:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('contact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contacs.contact')),
                ('work', models.CharField(max_length=250)),
            ],
            bases=('contacs.contact',),
        ),
    ]
