from django.contrib import messages
from django.db.models import Count
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView

from purbeurre.products.forms import ProductSearchForm
from purbeurre.products.models import Category, Product
from purbeurre.users.models import Favorite


def search_product(request):
    """Given an user input, the method retrieve a product from the database
    check if it exists, get the category where there is the most occurence and
    display the data in the template.

    Returns:
        [str]: List of the products from the same category
    """
    user_input = request.GET.get("product_search")
    # User input normalization
    user_input = str(user_input).lower().capitalize()

    try:
        # Retrieve PK for the product searched by user
        product_name = Product.objects.filter(name=user_input)[0]
        product = Product.objects.get(pk=product_name.pk)

        # Getting all categories matching the product
        categories = Category.objects.filter(categories__name=product.name)

        # Finding products matching the same categories
        categories_all = Product.objects.filter(categories__in=categories)

        # Count the total of categories being find matching the product
        categories_count = categories_all.annotate(count_cat=Count("categories"))

        # Return number of categories greater than or equal to the categories in product
        categories_filter = categories_count.filter(count_cat__gte=4)

        # Get products than have a lower nutriscore than the one search by user
        product_filter = categories_filter.filter(
            nutriscore_grade__lte=product.nutriscore_grade
        )

        # display products from the healthier to the worst
        sub_results = product_filter.order_by("nutriscore_grade")[:6]

        context = {"product": sub_results, "origin_product": product_name}
        return render(request, "products/product.html", context)
    except IndexError:
        messages.error(
            request, (f"Impossible de trouver des substitutes à {user_input}")
        )
        return redirect("/")


class ProductDetailView(DetailView):
    """Detail view that lists display information for a given <Model> on a single page
    Args:
        DetailView : Render a "detail" view of an object.
    """

    model = Product


def save_favorite(request):
    """Save a Substituer for a product and redirct user to
    the favoris view

    Args:
        id_product (int): Id of the product to be saved
    """
    user = request.user
    product_id = request.POST.get("product_id")
    substitute_id = request.POST.get("substitute_id")

    origin_product = Product.objects.get(pk=product_id)
    product = Product.objects.get(pk=substitute_id)

    Favorite.objects.create(product=origin_product, substitute=product, user=user)
    return redirect("users:fav", user)
