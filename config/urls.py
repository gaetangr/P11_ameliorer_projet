from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

urlpatterns = [
    # Enable user to change language:
    # https://docs.djangoproject.com/en/3.1/topics/i18n/translation/#the-set-language-redirect-view
    path("i18n/", include("django.conf.urls.i18n")),
    path(
        "",
        TemplateView.as_view(template_name="pages/home.html"),
        name="home",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("purbeurre.users.urls", namespace="users"),
    ),
    path(
        "products/",
        include("purbeurre.products.urls", namespace="products"),
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

project_name = "Pur Beurre "
admin.site.site_header = f"{project_name} - Web Plateform"
admin.site.site_title = f"{project_name} Admin Portal"
admin.site.index_title = f"Welcome to {project_name} Admin Portal"
