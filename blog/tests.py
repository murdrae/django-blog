from django.test import TestCase
from models import Post
# Create your tests here.

class PostTest(TestCase):
	def test_str(self):
		my_title = Post(title='This is a basic title for a basic test case')
		self.assertEquals(str(my_title), 'This is a basic title for a basic test case',)
