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

class IngredientsListView(ListView):
	model = Ingredient
	context_object_name = 'ingredients'
	template_name = 'main/ingredients.html'

def new_ingredient(request):
    context = dict()
    form = NewIngredientForm()
    if request.method == 'POST':
        form = NewIngredientForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]

            i = Ingredient(name=name)
            i.save()

            return redirect('../')

        else:
            pass

    template = 'main/new_ingredient.html'
    context['form'] = form

    return render(request, template, context)

class BeefCowGroupListView(ListView):
	model = BeefCowGroup
	context_object_name = 'beef_cow_groups'
	template_name = 'main/beef_cow_groups.html'

def new_beef_cow_group(request):
    context = dict()
    form = NewBeefCowGroupForm()
    if request.method == 'POST':
        form = NewBeefCowGroupForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            average_meat_output = form.cleaned_data["average_meat_output"]

            bcg = BeefCowGroup(name=name, average_meat_output=average_meat_output)
            bcg.save()

            return redirect('../')

        else:
            pass

    template = 'main/new_beef_cow_group.html'
    context['form'] = form

    return render(request, template, context)

class DairyCowGroupListView(ListView):
	model = DairyCowGroup
	context_object_name = 'dairy_cow_groups'
	template_name = 'main/dairy_cow_groups.html'

def new_dairy_cow_group(request):
    context = dict()
    form = NewDairyCowGroupForm()
    if request.method == 'POST':
        form = NewDairyCowGroupForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            average_milk_production = form.cleaned_data["average_milk_production"]

            dcg = DairyCowGroup(name=name, average_milk_production=average_milk_production)
            dcg.save()

            return redirect('../')

        else:
            pass

    template = 'main/new_dairy_cow_group.html'
    context['form'] = form

    return render(request, template, context)

class ChickenGroupListView(ListView):
	model = ChickenGroup
	context_object_name = 'chicken_groups'
	template_name = 'main/chicken_groups.html'

def new_chicken_group(request):
    context = dict()
    form = NewChickenGroupForm()
    if request.method == 'POST':
        form = NewChickenGroupForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            average_meat_output = form.cleaned_data["average_meat_output"]

            cg = ChickenGroup(name=name, average_meat_output=average_meat_output)
            cg.save()

            return redirect('../')

        else:
            pass

    template = 'main/new_chicken_group.html'
    context['form'] = form

    return render(request, template, context)

class GoatGroupListView(ListView):
	model = GoatGroup
	context_object_name = 'goat_groups'
	template_name = 'main/goat_groups.html'

def new_goat_group(request):
    context = dict()
    form = NewGoatGroupForm()
    if request.method == 'POST':
        form = NewGoatGroupForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            average_milk_production = form.cleaned_data["average_milk_production"]

            gg = GoatGroup(name=name, average_milk_production=average_milk_production)
            gg.save()

            return redirect('../')

        else:
            pass

    template = 'main/new_goat_group.html'
    context['form'] = form

    return render(request, template, context)

class PigGroupListView(ListView):
	model = PigGroup
	context_object_name = 'pig_groups'
	template_name = 'main/pig_groups.html'

def new_pig_group(request):
    context = dict()
    form = NewPigGroupForm()
    if request.method == 'POST':
        form = NewPigGroupForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            average_meat_output = form.cleaned_data["average_meat_output"]

            pg = PigGroup(name=name, average_meat_output=average_meat_output)
            pg.save()

            return redirect('../')

        else:
            pass

    template = 'main/new_pig_group.html'
    context['form'] = form

    return render(request, template, context)