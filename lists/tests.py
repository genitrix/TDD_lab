from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page # (2)
# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolve_to_home_page_view(self):
		found = resolve('/') # (1)
		self.assertEqual(found.func, home_page) # (1)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do lists</title>', html)
		self.assertTrue(html.endswith('</html>'))

# class SmokeTest(TestCase):
#
# 	def test_bad_maths(self):
# 		self.assertEqual(1+1, 3)