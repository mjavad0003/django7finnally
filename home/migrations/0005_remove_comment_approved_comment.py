# Generated by Django 4.0 on 2024-06-04 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_comment_approved_comment_alter_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]
