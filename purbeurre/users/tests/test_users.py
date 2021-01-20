""" Functional test for registration and login user behavior """
import sys
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver

from config.settings.base import BASE_DIR

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1920x1080")


class TestUserBehavior(StaticLiveServerTestCase):
    """Functional test for the login and registeration behiavor"""

    @classmethod
    def setUpClass(cls):
        """Setting up tests variables and config"""
        super().setUpClass()
        cls.browser = webdriver.Chrome(
            executable_path=str(BASE_DIR / "webdrivers" / "chromedriver"),
            options=chrome_options,
        )
        cls.username = "Gaetan"
        cls.email = "hello@gaetangr.me"
        cls.password = "you-will-never-guess"
        cls.browser.implicitly_wait(10)
        cls.browser.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.quit()

    def test_if_user_can_register_and_login(self):
        """User should be able to register, login and then access their profil page"""

        # Accessing live server
        self.browser.get(self.live_server_url)

        # Accesing registeration page and filling out information
        self.browser.find_element_by_css_selector("#sign-up-link").click()
        self.browser.find_element_by_css_selector("#id_username").send_keys(
            self.username
        )
        self.browser.find_element_by_css_selector("#id_password1").send_keys(
            self.password
        )
        self.browser.find_element_by_css_selector("#id_password2").send_keys(
            self.password
        )
        time.sleep(3)
        self.browser.find_element_by_css_selector("#id_email").send_keys(self.email)
        self.browser.find_element_by_css_selector("#button-submit").click()

        # Loging in
        self.browser.find_element_by_css_selector("#id_username").send_keys(
            self.username
        )
        self.browser.find_element_by_css_selector("#id_password").send_keys(
            self.password
        )
        self.browser.find_element_by_css_selector("#button-submit").click()

        # Accessing user profile
        self.browser.find_element_by_css_selector("#user-detail").click()
