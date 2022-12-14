# Generated by Django 4.1.3 on 2022-11-20 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0008_remove_beefcowgroupingredients_beef_cow_group_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BeefCowGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('average_meat_output', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='ChickenGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('average_meat_output', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='DairyCowGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('average_milk_production', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GoatGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('average_milk_production', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='PigGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('average_meat_output', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='PigGroupIngredients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ingredient')),
                ('pig_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.piggroup')),
            ],
        ),
        migrations.CreateModel(
            name='GoatGroupIngredients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('goat_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.goatgroup')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='FeedBatch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chicken_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.chickengroup')),
                ('dairy_cow_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.dairycowgroup')),
                ('goat_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.goatgroup')),
                ('pig_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.piggroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.authuser')),
            ],
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.djangocontenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.authuser')),
            ],
        ),
        migrations.CreateModel(
            name='DairyCowGroupIngredients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dairy_cow_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dairycowgroup')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='ChickenGroupIngredients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chicken_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.chickengroup')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='BeefCowGroupIngredients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('beef_cow_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.beefcowgroup')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.authpermission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.authuser')),
            ],
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.authgroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.authuser')),
            ],
        ),
        migrations.AddField(
            model_name='authpermission',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.djangocontenttype'),
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.authgroup')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.authpermission')),
            ],
        ),
    ]
