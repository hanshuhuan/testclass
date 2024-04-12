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

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')