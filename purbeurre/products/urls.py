from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    path("save", views.save_favorite, name="save"),
    path("", views.search_product, name="prod"),
    path(route="<int:pk>", view=views.ProductDetailView.as_view(), name="detail"),
]
