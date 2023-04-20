from django.shortcuts import render, get_object_or_404
from http.client import HTTPResponse
from django.views.generic import TemplateView, ListView
from .models import State, Activity
from django.db.models import Q
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from tablib import Dataset
from .resources import ActivityResource
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = State
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Activity.objects.filter(Q(state__iexact=query))
        #state_name = Activity.objects.get(state_name='state')
        return object_list
    
def Import_Excel_pandas(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        activityExcelData = pd.read_excel(filename)
        dbframe = activityExcelData
        for dbframe in dbframe.itertuples():
            obj = Activity.objects.create(state = dbframe.state, abv = dbframe.abv, name = dbframe.name, category = dbframe.category, image = dbframe.image, link = dbframe.link, description = dbframe.description, address = dbframe.address)
            obj.save()
        return render(request, 'Import_excel_db.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'Import_excel_db.html', {})

def Import_excel(request):
    if request.method == 'POST':
        Activity = ActivityResource()
        dataset = Dataset()
        new_activity = request.FILES['myfile']
        data_import = dataset.load(new_activity.read())
        result = ActivityResource.import_data(dataset, dry_run = True)
        if not result.has_errors():
            ActivityResource.import_data(dataset, dry_run = False)
    return render(request, 'Import_excel_db.html', {})

def activity_listing(request, activity_id):
    activity = Activity.objects.get(pk = activity_id)
    favorited = bool
    if activity.favorite.filter(id = request.user.id).exists():
        favorited = True
    else:
        favorited = False
    return render(request, 'activity.html', {'activity' : activity, 'favorited' : favorited})
    
def FavoriteView(request, pk):
    activity = get_object_or_404(Activity, id = request.POST.get('activity_id'))
    if activity.favorite.filter(id = request.user.id).exists():
        activity.favorite.remove(request.user)
    else:
        activity.favorite.add(request.user)
    return HttpResponseRedirect(reverse('activity', args = [str(pk)]))

def FavoritesListView(request):
    new = Activity.objects.filter(favorite = request.user)
    return render(request, 'favorites.html', {'new' : new})