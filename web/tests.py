from django.test import TestCase
from django.urls import resolve
from web.views import home_page #(1)
from django.http import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') #(2)
        self.assertEqual(found.func, home_page) #(3)
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #(4)
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))