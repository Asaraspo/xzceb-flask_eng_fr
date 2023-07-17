import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def testTranslation(self):
        self.assertEqual(english_to_french('Hello'), 'Pepitoooo')

class TestFrenchToEnglish(unittest.TestCase):
    def testTranslation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()