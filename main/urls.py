from django.urls import path, include
from django.contrib import admin
from . import views as v


app_name = 'project'

urlpatterns = [
    path('', v.index, name='index'),

    path('feed_batches/',
        v.FeedBatchListView.as_view(),
        name='feed_batches'),

    path("feed_batches/new_batch/", 
        v.new_batch, 
        name="new_batch"),

    path('feed_groups/', 
        v.feed_groups,
        name='feed_groups'),
]
