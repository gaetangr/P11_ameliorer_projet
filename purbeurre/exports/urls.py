from django.url import path, include

from .views import FavoriteExportView

app_name = 'exports'

urlpatterns = [
    path('favorites/', FavoriteExportView.as_view(), name='favorites_csv')
]