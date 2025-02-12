# Generated by Django 5.1.6 on 2025-02-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aiexporiahome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.TextField(default='error 404'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(default='error 404'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='error 404', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='error 404', max_length=255),
        ),
    ]
