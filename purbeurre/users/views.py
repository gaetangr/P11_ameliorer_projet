import json.decoder

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DetailView,
    RedirectView,
    TemplateView,
    UpdateView,
)
from django.views.generic.edit import FormView

from .forms import UserRegistrationForm
from .models import Favorite

User = get_user_model()


class UserLoginView(SuccessMessageMixin, LoginView):
    """Connect an instance of :model:`users.User`
    and display a success message.

    Args:
        SuccessMessageMixin (class): Add a success message on successful form submission.
        LoginView (class): Display the login form and handle the login action.
    """

    form_class = AuthenticationForm
    template_name = "users/login.html"
    message = _("Welcome back !")
    success_message = message


user_login_view = UserLoginView.as_view()


class UserLogoutView(SuccessMessageMixin, LogoutView):
    """Logout an instance of :model:`users.User`
    and display a success message.

    Args:
        SuccessMessageMixin (class): Add a success message on successful form submission.
        LogoutView (class): Log out the user and display the 'You are logged out' message.
    """

    template_name = "users/logged_out.html"
    message = _("You logged out successfully !")
    success_message = message


user_logout_view = UserLogoutView.as_view()


class UserDetailView(LoginRequiredMixin, DetailView):
    """Detail view of an instance of :model:`users.User`

    Args:
        LoginRequiredMixin (class): Verify that the current user is authenticated.
        DetailView ([type]): Render a "detail" view of an object.
    """

    model = User
    # These Next Two Lines Tell the View to Index
    #   Lookups by Username
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorite"] = Favorite.objects.filter(user=self.request.user)
        return context


user_detail_view = UserDetailView.as_view()


class FavDetailView(LoginRequiredMixin, DetailView):
    """Detail view of an instance of :model:`users.User`

    Args:
        LoginRequiredMixin (class): Verify that the current user is authenticated.
        DetailView ([type]): Render a "detail" view of an object.
    """

    model = User
    # These Next Two Lines Tell the View to Index
    #   Lookups by Username
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/fav_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorite"] = Favorite.objects.filter(user=self.request.user)
        return context


fav_detail_view = FavDetailView.as_view()


class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """Update an instance of :model:`users.User`
    and display a success message.

    Args:
        SuccessMessageMixin (class): Add a success message on successful form submission.
        LoginRequiredMixin (class): Verify that the current user is authenticated.
        UpdateView (class): View for updating an object, with a response rendered by a template.
    """

    fields = ["username", "email", "bio"]
    model = User
    message = _("Welcome back !")
    success_message = "dekodzodzko"
    # Send the User Back to Their Own Page after a successful Update

    def get_success_url(self):
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username},
        )

    def get_object(self):
        # Only Get the User Record for the User Making the Request
        return User.objects.get(username=self.request.user.username)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username},
        )


user_redirect_view = UserRedirectView.as_view()


class UserCreateView(SuccessMessageMixin, CreateView):
    """Create a new instance of :model:`users.User`
    and display redirect to homepage.

    Args:
        SuccessMessageMixin (class): Add a success message on successful form submission.
        CreateView (class): View for creating a new object, with a response rendered by a template.
    """

    model = User
    form_class = UserRegistrationForm

    message = _("Your account has been created !")
    success_message = message


user_create_view = UserCreateView.as_view()
