from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from catalogue.models import (CatalogueItem, BoardGameItem, BoardGameCommodity)
from catalogue.forms import BoardGameItemForm, BoardGameCommodityForm
from django.views.generic import (ListView,DetailView,CreateView, UpdateView)
from django.conf import settings

# Create your views here.
class CatalogueItemListView(ListView):
    queryset = BoardGameItem.objects.all().order_by("itemLabel")
    filter_criteria = ""
    context_object_name = 'catalogueitem_list'
    template_name = 'catalogue/catalogueitem_list.html'
    paginate_by = settings.CATALOGUE_PAGINATION
    paginate_orphans = settings.CATALOGUE_PAGINATION_ORPHANS


    def get_queryset(self):
        if self.request.method == 'GET':

            self.filter_criteria = self.request.GET.get("filter")
            if self.filter_criteria:
                search_type = self.request.GET.get("search")
                if search_type == "barcode":
                    commodities_ids = BoardGameCommodity.objects.filter(codeValue__startswith=self.filter_criteria).values_list('catalogueEntry')
                    self.queryset = BoardGameItem.objects.filter(id__in=commodities_ids).order_by("itemLabel")
                    # self.queryset = BoardGameItem.objects.filter(boardgamecommodity__codeValue__startswith=self.filter_criteria).order_by("codeValue")
                elif search_type == "title":
                    self.queryset =  BoardGameItem.objects.filter(itemLabel__icontains=self.filter_criteria).order_by("itemLabel")
                # else:
                #     objects =  self.model.objects.all().order_by("-itemLabel")
            return self.queryset


# class CatalogueItemFilteredListView(CatalogueItemListView):
#     filterCriteria = ""
#     def get_queryset(self):
#         return BoardGameItem.objects.all().order_by("itemLabel")


class BoardGameItemDetailsView(DetailView):
    model = BoardGameItem

class BoardGameItemCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    #authorization restriction section
    # login_url = 'accounts/login/'
    permission_required = 'catalogue.add_boardgameitem'
    raise_exception=True

    form_class = BoardGameItemForm
    model = BoardGameItem

class BoardGameItemUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    #authorization restriction section
    permission_required = 'catalogue.change_boardgameitem'
    raise_exception=True
    # login_url = 'accounts/login/'

    form_class = BoardGameItemForm
    model = BoardGameItem
    
############################################
# Client Views
############################################
class RentalClientListView(ListView):
    model = RentalClient

    def get_queryset(self):
        return RentalClient.objects.all()
        # .orderby('itemLabel')
        
class RentalClientDetailsView(DetailView):
    model = RentalClient
    
class RentalClientCreateView(CreateView):
    #authorization restriction section
    # login_url = '/login/'
    # redirect_field_name = todo define it

    form_class = RentalClientForm
    model = RentalClient

##########################################
# BoardGameItem additional views
##########################################
@login_required
@permission_required('catalogue.add_boardgameitem', raise_exception=True)
def repeat_add_boardgame(request):
    if request.method == 'POST':
        form = BoardGameItemForm(request.POST)
        if form.is_valid():
            boardgame = form.save(commit=False)
            boardgame.save()
    return redirect('boardgame_new')

@login_required
@permission_required('catalogue.add_boardgameitem', raise_exception=True)
def boardgamelist_return(request):
    if request.method == 'POST':
        form = BoardGameItemForm(request.POST)
        if form.is_valid():
            boardgame = form.save(commit=False)
            boardgame.save()
    return redirect('catalogue_entries')


@login_required
@permission_required('catalogue.add_boardgameitem', raise_exception=True)
def return_home (request):
    if request.method == 'POST':
        form = BoardGameItemForm(request.POST)
        if form.is_valid():
            boardgame = form.save(commit=False)
            boardgame.save()
    return redirect('welcome')


class BoardGameCommodityCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    #authorization restriction section
    # login_url = 'accounts/login/'
    permission_required = 'catalogue.add_boardgamecommodity'
    raise_exception=True

    form_class = BoardGameCommodityForm
    model = BoardGameCommodity
    template_name = 'catalogue/boardgamecommodity_form.html'

    initial = {}

    def get(self, request, *args, **kwargs):
        if 'bgpk' in kwargs:
            self.initial ['catalogueEntry'] = kwargs ['bgpk']
        else:
            self.initial ['catalogueEntry'] = None
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

class BoardGameCommodityUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    #authorization restriction section
    permission_required = 'catalogue.change_boardgamecommodity'
    raise_exception=True
    # login_url = 'accounts/login/'

    form_class = BoardGameCommodityForm
    model = BoardGameCommodity
