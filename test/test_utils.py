import unittest
from utils import Utils

class UtilsTests(unittest.TestCase):

	def testExample(self):
		utils = Utils()
		self.assertEqual(utils.example(), True)

if __name__ == '__main__':
	unittest.main()