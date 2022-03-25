# Generated by Django 4.0.3 on 2022-03-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourapp', '0002_rename_neighbour_neighbourhood'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='health_info',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='health_officer',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='police_info',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='police_officer',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
