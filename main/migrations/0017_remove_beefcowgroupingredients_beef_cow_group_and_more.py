# Generated by Django 4.1.3 on 2022-11-20 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beefcowgroupingredients',
            name='beef_cow_group',
        ),
        migrations.RemoveField(
            model_name='beefcowgroupingredients',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='chickengroupingredients',
            name='chicken_group',
        ),
        migrations.RemoveField(
            model_name='chickengroupingredients',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='dairycowgroupingredients',
            name='dairy_cow_group',
        ),
        migrations.RemoveField(
            model_name='dairycowgroupingredients',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='feedbatch',
            name='chicken_group',
        ),
        migrations.RemoveField(
            model_name='feedbatch',
            name='dairy_cow_group',
        ),
        migrations.RemoveField(
            model_name='feedbatch',
            name='goat_group',
        ),
        migrations.RemoveField(
            model_name='feedbatch',
            name='pig_group',
        ),
        migrations.RemoveField(
            model_name='goatgroupingredients',
            name='goat_group',
        ),
        migrations.RemoveField(
            model_name='goatgroupingredients',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='piggroupingredients',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='piggroupingredients',
            name='pig_group',
        ),
        migrations.DeleteModel(
            name='BeefCowGroup',
        ),
        migrations.DeleteModel(
            name='BeefCowGroupIngredients',
        ),
        migrations.DeleteModel(
            name='ChickenGroup',
        ),
        migrations.DeleteModel(
            name='ChickenGroupIngredients',
        ),
        migrations.DeleteModel(
            name='DairyCowGroup',
        ),
        migrations.DeleteModel(
            name='DairyCowGroupIngredients',
        ),
        migrations.DeleteModel(
            name='FeedBatch',
        ),
        migrations.DeleteModel(
            name='GoatGroup',
        ),
        migrations.DeleteModel(
            name='GoatGroupIngredients',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='PigGroup',
        ),
        migrations.DeleteModel(
            name='PigGroupIngredients',
        ),
    ]
