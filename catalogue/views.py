from django.shortcuts import render
# from django.contrib.auth.mixins import LoginRequiredMixin
from catalogue.models import (CatalogueItem, BoardGameItem, Warehouse, Container)
from catalogue.forms import BoardGameForm, WarehouseForm, ContainerForm
from django.views.generic import (ListView,DetailView,CreateView, UpdateView)

# Create your views here.
class CatalogueItemListView(ListView):
    model = BoardGameItem

    def get_queryset(self):
        return BoardGameItem.objects.all()
        # .orderby('itemLabel')

class BoardGameDetailsView(DetailView):
    model = BoardGameItem

# todo: add LoginRequiredMixin inheritance
class BoardGameCreateView(CreateView):
    #authorization restriction section
    # login_url = '/login/'
    # redirect_field_name = todo define it

    form_class = BoardGameForm
    model = BoardGameItem

# todo: add LoginRequiredMixin inheritance
class BoardGameUpdateView(UpdateView):
    #authorization restriction section
    # login_url = '/login/'
    # redirect_field_name = todo define it

    model = BoardGameItem


class WarehouseListView(ListView):
    model = Warehouse

    def get_queryset(self):
        return Warehouse.objects.all()


class WarehouseDetailView(DetailView):
    model = Warehouse


class WarehouseCreateView(CreateView):
    model = Warehouse
    form_class = WarehouseForm


class ContainerCreateView(CreateView):
    model = Container
    form_class = ContainerForm
