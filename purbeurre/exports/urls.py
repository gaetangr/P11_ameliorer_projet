
from django.urls import path

from . import views

app_name = 'exports'

urlpatterns = [
    path('favorites/', view=views.FavoriteExportView.as_view(), name='favorites_csv')
]