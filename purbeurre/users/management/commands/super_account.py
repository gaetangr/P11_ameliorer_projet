# flake8: noqa
import time

import crayons
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from halo import Halo

from purbeurre.users.models import User


class Command(BaseCommand):
    """Creating a superuser for the admin panel with prepopulated datas"""

    help = "Creating a superuser for the admin panel with prepopulated datas"

    def handle(self, *args, **options):
        spinner = Halo(
            text="Creating super user..", text_color="yellow", spinner="dots"
        )
        spinner.start()
        time.sleep(3)
        admin_url = f"http://127.0.0.1:8000/{settings.ADMIN_URL}"
        default_password = "password"
        default_username = "dmin"
        try:
            user = User.objects.create_user(
                username=default_username,
                password=default_password,
                first_name="John",
                last_name="Doe",
                is_superuser=True,
                is_staff=True,
                email="admin@admin.com",
            )
            spinner.succeed(crayons.green("Success!"))
            print(
                crayons.normal(
                    f"ℹ Username: {crayons.yellow(default_username)} - Password: {crayons.yellow(default_password)} - Connect to: {crayons.yellow(admin_url)} \n"
                )
            )
        except IntegrityError:
            spinner.fail(
                crayons.red(
                    "The superuser has already been created! use command: 'python manage.py createsuperuser'"
                )
            )
