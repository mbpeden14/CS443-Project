# Generated by Django 4.1.3 on 2022-11-20 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_authpermission_content_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authusergroups',
            name='group',
        ),
        migrations.RemoveField(
            model_name='authusergroups',
            name='user',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
    ]
