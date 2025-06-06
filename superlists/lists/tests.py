from django.test import TestCase
from django.urls import resolve
from lists.views import bosh_sahifa
from django.http import HttpRequest

# Create your tests here.

class BoshSahifa(TestCase):
    def test_bosh_sahifa(self):
        found = resolve('/')
        self.assertEqual(found.func, bosh_sahifa)
    
    def test_bosh_sahifa_modullari(self):
        request = HttpRequest()
        response = bosh_sahifa(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_bosh_sahifa_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'bosh_sahifa.html')
    
    def test_yangi_ish_yaratish(self):
        response = self.client.post('/', data={'iteam-text': "Yangi ish"})
        self.assertIn('Yangi ish', response.content.decode())



