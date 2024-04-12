from urllib import response
from django.test import TestCase
from django.urls import resolve
from web.views import home_page #(1)
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.
class HomePageTest(TestCase):  
    def test_uses_home_template(self):
        response = self.client.get('/') #(4)
        self.assertTemplateUsed(response, 'home.html') #(5)