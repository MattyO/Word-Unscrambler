import string
class Dictonary:

	def __init__(self, filename):
		self._dictionary = dict()
		dicFile = open(filename,'r')
		for line in dicFile: 
			self._dictionary[line.rstrip('\n').lower()] = {'size': len(line), 'makeup': None}
	def _makeup(self, word): 
		rMakeup = None
		if not self._isCached(word):
			occurances = self._calcMakeup(word)
			self._cacheMakup(word, occurances)

		rMakeup = self._getCacheMakup(word)	
		return rMakeup

	def _calcMakeup(self, word):
		rOccurances = dict()
		for letter in string.lowercase: 
			if word.count(letter) > 0: 
				rOccurances[letter] = word.count(letter)
		return rOccurances

	def _isCached(self, word): 
		rIsCached = False
		if self._dictionary[word]['makeup'] != None: 
			rIsCached = True
		return rIsCached
	def _cacheMakup(self, word, makeup):	
		self._dictionary[word]['makeup'] = makeup
	def _getCacheMakup(self, word):
		return self._dictionary[word]['makeup'] 	
	def _getWordsOfSize(self, size):
		rWords = set()
		for word in self._dictionary: 
			if len(word) == size: 
				rWords.add(word)
		return rWords
	def unscramble(self, word):
		rUnscrambled = set()
		possibleWords = self._getWordsOfSize(len(word))
		currentWordMakeup = self._calcMakeup(word)
		for word in possibleWords: 
			if currentWordMakeup == self._makeup(word):
				rUnscrambled.add(word)
		return rUnscrambled

