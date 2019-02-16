from django.test import TestCase
from .models import CustomUser

class UserTest(TestCase):
	def setUp(self):
		'''Membuat test case sendiri'''
		CustomUser.objects.create(first_name='kevin', last_name='asyraf')
		CustomUser.objects.create(username='kevin.trap')

	def test_correct_first_name(self):
		'''mengecek apakah first_name benar'''
		kevin = CustomUser.objects.get(first_name='kevin')
		self.assertEqual(kevin.first_name, 'kevin')

	def test_correct_last_name(self):
		'''mengecek apakah last_name benar'''
		asyraf = CustomUser.objects.get(last_name='asyraf')
		self.assertEqual(asyraf.last_name, 'asyraf')

	def test_correct_username(self):
		'''mengecek apakah username benar'''
		trap = CustomUser.objects.get(username='kevin.trap')
		self.assertEqual(trap.username, 'kevin.trap')



