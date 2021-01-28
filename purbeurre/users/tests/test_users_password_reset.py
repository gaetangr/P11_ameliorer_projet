""" Functional test for registration and login user behavior """
import sys
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from django.test import TestCase
from django.core import mail

from config.settings.base import BASE_DIR

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1920x1080")


class TestUserRequestPasswordBehavior(StaticLiveServerTestCase):
    """Functional test for the reset password behiavor"""

    @classmethod
    def setUpClass(cls):
        """Setting up tests variables and config"""
        super().setUpClass()
        cls.browser = webdriver.Chrome(
            executable_path=str(BASE_DIR / "webdrivers" / "chromedriver"),
            options=chrome_options,
        )
        cls.email = "hello@gaetangr.me"
        cls.browser.implicitly_wait(10)
        cls.browser.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.quit()

    def test_if_user_can_request_new_password(self):
        """User should be able to request a new password"""

        # Accessing password reset view
        self.browser.get("http://127.0.0.1:8000/reset_password/")

        # Sending email for reset
        self.browser.find_element_by_css_selector("#id_email").send_keys(
            self.email
        )
        self.browser.find_element_by_css_selector("#button-submit").click()
        time.sleep(7.1)
        self.assertEqual(len(mail.outbox), 1)
