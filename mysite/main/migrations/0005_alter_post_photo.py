# Generated by Django 4.1 on 2023-03-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_post_git'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
