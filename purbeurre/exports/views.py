import csv

from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from purbeurre.users.models import Favorite


class FavoriteExportView(LoginRequiredMixin, View):
    """Exports favorites as a CSV file."""

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/html')
        response['Content-Disposition'] = f'attachment; filename="{request.user}_favorites.csv"'
        favorites = Favorite.objects.filter(user=request.user)
        fieldnames = [
            'product_id',
            'product_code',
            'product_name',
            'product_nutriscore',
            'product_url',
            'substitute_id',
            'substitute_code',
            'substitute_name',
            'substitute_nutriscore',
            'substitute_url',
        ]
        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()
        for favorite in favorites:
            writer.writerow(favorite.as_dict())
        return response
