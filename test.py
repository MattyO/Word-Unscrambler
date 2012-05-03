import unittest
from Dictonary import Dictonary

class testAll(unittest.TestCase): 

	def setUp(self):
		self.testdic = Dictonary('wordlist')
	def test_calcMakup(self):
		self.assertEqual({'t':2, 'e':1, 's':1}, self.testdic._calcMakeup('test'))
	def test_wordMakeup(self):
		self.assertEqual({'t':2, 'e':1, 's':1}, self.testdic._makeup('test'))
		self.assertEqual({'t':2, 'e':1, 's':2}, self.testdic._makeup('tests'))
	def test_unscramble(self):
		self.assertEqual({'bubble'}, self.testdic.unscramble('bbuleb'))
		self.assertEqual({'flower', 'fowler'}, self.testdic.unscramble('lwrfoe'))
		self.assertEqual({'cake'}, self.testdic.unscramble('kaec'))
		self.assertEqual({'water'}, self.testdic.unscramble('rtawe'))
		self.assertEqual({'cork', 'rock','kroc'}, self.testdic.unscramble('cokr'))
		self.assertEqual({'milk'}, self.testdic.unscramble('kmli'))
		self.assertEqual({'peace'}, self.testdic.unscramble('pcaee'))
if __name__ == '__main__': 
	unittest.main()
		
		
		
		
