from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import *
from .models import *
from django.forms import ValidationError

# Create your views here.

def index(request):
    context = {}

    return render(request, 'main/index.html', context=context)

def feed_groups(request):
    context = {}

    return render(request, 'main/feed_groups.html', context=context)

class FeedBatchListView(ListView):
	model = FeedBatch
	context_object_name = 'feed_batches'
	template_name = 'main/feed_batches.html'

def new_batch(request):
    context = dict()
    form = NewFeedBatchForm()
    if request.method == 'POST':
        form = NewFeedBatchForm(request.POST)

        if form.is_valid():
            dairy_cow_group = form.cleaned_data["dairy_cow_group"]
            beef_cow_group = form.cleaned_data["beef_cow_group"]
            chicken_group = form.cleaned_data["chicken_group"]
            goat_group = form.cleaned_data["goat_group"]
            pig_group = form.cleaned_data["pig_group"]

            vals = [dairy_cow_group, beef_cow_group, chicken_group, goat_group, pig_group]

            count = 0;
            for i in range(len(vals)):
                if vals[i] is not None:
                    count = count + 1

            if (count > 1):
                raise ValidationError("ERROR: Multiple group values received - only one needed.")

            user = AuthUser.objects.get(id=request.user.id)

            fb = FeedBatch(user=user, dairy_cow_group=dairy_cow_group, beef_cow_group=beef_cow_group, chicken_group=chicken_group, goat_group=goat_group, pig_group=pig_group)
            fb.save()

            return redirect('../')

        else:
            pass

    template = 'main/new_batch.html'
    context['form'] = form

    return render(request, template, context)