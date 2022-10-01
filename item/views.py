from django.views import generic
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q

from item.forms import CreateItemForm, CreateImageFormset
from item.models import Item, ManyImage


def index_page(request):
    title = request.GET.get('title')
    items = Item.objects.all()
    if title:
        items = Item.objects.filter(Q(brand__icontains=title) | Q(description__icontains=title))
    return render(request, "index.html", locals())


class CreateItemView(generic.CreateView):
    template_name = 'create_item.html'
    model = Item
    form_class = CreateItemForm

    def post(self, request, *args, **kwargs):
        item_form = CreateItemForm(request.POST, prefix='item_form')
        formset = CreateImageFormset(request.POST, request.FILES,
                                     queryset=ManyImage.objects.none(), prefix='image_form')

        if item_form.is_valid() and formset.is_valid():
            item = item_form.save(commit=False)
            item.save()

            images = formset.save(commit=False)
            for image in images:
                image.item_img = item
                image.save()

            return HttpResponseRedirect(self.get_success_url())

    def get(self, request, *args, **kwargs):
        item_form = CreateItemForm(prefix='item_form')
        formset = CreateImageFormset(queryset=ManyImage.objects.none(), prefix='image_form')

        return render(request, 'create_item.html', {'item_form': item_form, 'image_form': formset})

    def get_success_url(self):
        return reverse('index')


class DetailItemView(generic.DetailView):
    template_name = 'detail_item.html'
    model = Item
    context_object_name = 'item'