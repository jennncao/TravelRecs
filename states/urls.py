from django.urls import path
from.views import HomePageView, SearchResultsView, FavoriteView, FavoritesListView
from . import views
from travelrecs import settings
from django.conf.urls.static import static

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name = "search_results"),
    path('', HomePageView.as_view(), name = "home"),
    path('import/', views.Import_Excel_pandas, name = 'travelrecs_pandas'),
    path('Import_Excel_pandas/', views.Import_Excel_pandas, name = 'travelrecs_pandas'),
    path('Import_excel', views.Import_excel, name = 'Import_excel'),
    path('activity/<activity_id>', views.activity_listing, name = "activity"),
    path('favorite/<int:pk>', FavoriteView, name = 'favorite'), 
    path('favorites/', FavoritesListView, name = 'favoritesList'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)