# Generated by Django 4.1 on 2023-03-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='git',
            field=models.URLField(max_length=900, null=True),
        ),
    ]
