from django.contrib import admin
from .import models as models

# Register your models here.

admin.site.register(models.FeedBatch)
admin.site.register(models.Ingredient)

admin.site.register(models.BeefCowGroup)
admin.site.register(models.DairyCowGroup)
admin.site.register(models.ChickenGroup)
admin.site.register(models.GoatGroup)
admin.site.register(models.PigGroup)

admin.site.register(models.BeefCowGroupIngredients)
admin.site.register(models.DairyCowGroupIngredients)
admin.site.register(models.ChickenGroupIngredients)
admin.site.register(models.GoatGroupIngredients)
admin.site.register(models.PigGroupIngredients)