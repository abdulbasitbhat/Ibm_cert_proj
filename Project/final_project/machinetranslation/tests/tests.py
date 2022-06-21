import sys
sys.path.append("..")
from translator import english_to_french, french_to_english
import unittest
import requests
import json

class TestMyModule(unittest.TestCase):
    def test_nullInputEnglishToFrench(self):
        self.assertMultiLineEqual(json.dumps(english_to_french(' ')),json.dumps({'translations': [{'translation': ' '}], 'word_count': 0, 'character_count': 1}))
    def test_nullInputFrenchToEnglish(self):
        self.assertMultiLineEqual(json.dumps(french_to_english(' ')),json.dumps({'translations': [{'translation': ' '}], 'word_count': 0, 'character_count': 1}))

    def test_englishToFrench(self):
        self.assertMultiLineEqual(json.dumps(english_to_french('hello')),json.dumps({'translations': [{'translation': 'Bonjour'}], 'word_count': 1, 'character_count': 5}))

    def test_frenchToEnglish(self):
        self.assertMultiLineEqual(json.dumps(french_to_english('bonjour')),json.dumps({'translations': [{'translation': 'Hello'}], 'word_count': 1, 'character_count': 7}))

if __name__=='__main__':
    unittest.main() 
