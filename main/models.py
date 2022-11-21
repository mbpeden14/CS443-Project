from django.db import models

# Create your models here.

# id field --> id = models.AutoField(primary_key=True)
# for short-medium strings --> str = models.CharField(max_length=125)
# for long strings --> str = models.TextField(max_length = 255)
# decimal numbers --> dec = models.DecimalField(max_digits=7, decimal_places=2)
# integers --> int = models.IntegerField()
# date --> date = models.DateField(auto_now = True)
# foreign key --> models.ForeignKey([model you are relating to], on_delete = models.CASCADE)

# EXAMPLE MODEL (Delete when finished with actual models) -->

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=125)
#     address = models.CharField(max_length=125)
#     age = models.CharField(max_length=3)
#     sex = models.CharField(max_length=6)
#     occupation = models.CharField(max_length=125)

#     class Meta:
#         managed = False
#         db_table = 'financial_system_user'

#     def __str__(self):
#         return self.name

# ACTUAL MODELS FOR PROJECT -->

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)

class DairyCowGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)
    average_milk_production = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

class DairyCowGroupIngredients(models.Model):
    id = models.AutoField(primary_key=True)
    dairy_cow_group = models.ForeignKey(DairyCowGroup, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)

class BeefCowGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)
    average_meat_output = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

class BeefCowGroupIngredients(models.Model):
    id = models.AutoField(primary_key=True)
    beef_cow_group = models.ForeignKey(BeefCowGroup, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)

class ChickenGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)
    average_meat_output = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

class ChickenGroupIngredients(models.Model):
    id = models.AutoField(primary_key=True)
    chicken_group = models.ForeignKey(ChickenGroup, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)

class PigGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)
    average_meat_output = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

class PigGroupIngredients(models.Model):
    id = models.AutoField(primary_key=True)
    pig_group = models.ForeignKey(PigGroup, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)

class GoatGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)
    average_milk_production = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

class GoatGroupIngredients(models.Model):
    id = models.AutoField(primary_key=True)
    goat_group = models.ForeignKey(GoatGroup, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)

class FeedBatch(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('AuthUser', on_delete = models.CASCADE)
    dairy_cow_group = models.ForeignKey(DairyCowGroup, on_delete = models.CASCADE, null=True, blank=True)
    beef_cow_group = models.ForeignKey(BeefCowGroup, on_delete = models.CASCADE, null=True, blank=True)
    chicken_group = models.ForeignKey(ChickenGroup, on_delete = models.CASCADE, null=True, blank=True)
    pig_group = models.ForeignKey(PigGroup, on_delete = models.CASCADE, null=True, blank=True)
    goat_group = models.ForeignKey(GoatGroup, on_delete = models.CASCADE, null=True, blank=True)