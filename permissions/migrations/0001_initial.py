# Generated by Django 2.2.4 on 2019-08-03 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0002_auto_20190803_2230'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('permissions_id', models.AutoField(primary_key=True, serialize=False)),
                ('ranking', models.PositiveSmallIntegerField(default=0, verbose_name='Rank')),
                ('djangogroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rankedpermissions', to='auth.Group', verbose_name='Django group')),
                ('researchgroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rankedpermissions', to='people.Group', verbose_name='Research group')),
            ],
            options={
                'ordering': ['djangogroup', 'researchgroup', 'ranking'],
            },
        ),
    ]
