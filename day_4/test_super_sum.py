'''Test suite for super_sum'''

from unittest import TestCase
from super_sum import super_sum

class SuperSumTestCase(TestCase):
	'''Test Case for super_sum'''

	def  test_empty_input(self):
		'''Test test_empty_input'''
		self.assertEqual(super_sum(),0)

	"""def test_array_input(self):
		'''Test sum of numbers in an array'''
		a = [2,3,4]
		self.assertEqual(super_sum(a),9)"""

	def test_sum_of_integers(self):
		'''Test sum of integers'''
		#super_sum(1,2,3)
		self.assertEqual(super_sum(1, 2, 3), 6)
		self.assertNotEqual(super_sum(10, 20, 30), 100)

	def test_sum_of_items_in_a_list(self):
		'''Test sum of items in a single list'''
		self.assertEqual(super_sum([1,2,3]),6)

	def test_string_input_returns(self):
		'''Test string input returns 0'''

		self.assertEqual(super_sum(""), 0)


	