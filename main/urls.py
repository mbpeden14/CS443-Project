from django.urls import path, include
from django.contrib import admin
from . import views as v


app_name = 'project'

urlpatterns = [
    path('', v.index, name='index'),

    path('feed_batches/',
        v.FeedBatchListView.as_view(),
        name='feed_batches'),

    path('ingredients/',
        v.IngredientsListView.as_view(),
        name='ingredients'),

    path("ingredients/new_ingredient/", 
        v.new_ingredient, 
        name="new_ingredient"),

    path('beef_cow_groups/',
        v.BeefCowGroupListView.as_view(),
        name='beef_cow_groups'),

    path("beef_cow_groups/new_group/", 
        v.new_beef_cow_group, 
        name="new_beef_cow_group"),

    path('dairy_cow_groups/',
        v.DairyCowGroupListView.as_view(),
        name='dairy_cow_groups'),

    path("dairy_cow_groups/new_group/", 
        v.new_dairy_cow_group, 
        name="new_dairy_cow_group"),

    path('chicken_groups/',
        v.ChickenGroupListView.as_view(),
        name='chicken_groups'),

    path("chicken_groups/new_group/", 
        v.new_chicken_group, 
        name="new_chicken_group"),

    path('goat_groups/',
        v.GoatGroupListView.as_view(),
        name='goat_groups'),

    path("goat_groups/new_group/", 
        v.new_goat_group, 
        name="new_goat_group"),

    path('pig_groups/',
        v.PigGroupListView.as_view(),
        name='pig_groups'),

    path("pig_groups/new_group/", 
        v.new_pig_group, 
        name="new_pig_group"),

    path("feed_batches/new_batch/", 
        v.new_batch, 
        name="new_batch"),

    path('feed_groups/', 
        v.feed_groups,
        name='feed_groups'),
]
