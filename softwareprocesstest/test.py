import unittest

from softwareprocess.convertString2Dictionary import convertString2Dictionary

# inputString =  'key1%3Dvalue%3B%20key2%3Dvalue'
# result = convertString2Dictionary(inputString)
# print(result)

class TestConvertString2Dictionary(unittest.TestCase):
    def testConvertString2Dictionary(self):
        expected = {
            'function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse': {'function': 'calculatePosition', 'sighting': 'Betelgeuse'},
            'abc%3D123': {'abc': '123'},
            'function%20%3D%20get_stars': {'error': 'true'},
            'key%3Dvalue%2C%20key%3Dvalue': {'error': 'true'},
            'key%3D': {'error': 'true'},
            'value': {'error': 'true'},
            '1key%3Dvalue': {'error': 'true'},
            'k%20e%20y%20%3D%20value': {'error': 'true'},
            '': {'error': 'true'},
            'key1%3Dvalue%3B%20key2%3Dvalue': {'error': 'true'},
            '%20key%3Dvalue ': {'key': 'value'},
            '%3Dkey': {'error': 'true'},
            '%3Dkey%3Dvalue': {'error': 'true'},
            'key%3Dvalue%3Dkey1%3Dvalue2': {'error': 'true'},
            'key%3D%3Dvalue%20': {'error': 'true'},
            'key%Dvalue%3D': {'error': 'true'},
            '.key%3Dvalue': {'error': 'true'},
            'ke.y%3Dvalue': {'ke.y': 'value'},
            'ke.y%3D.v.a.lue': {'ke.y': '.v.a.lue'},
            'ke.y%3D%20.v.a.lue': {'ke.y': '.v.a.lue'},
            'ke.y%3D%20.%20v.a.lue': {'error': 'true'},
        }
        for input, expected in expected.iteritems():
            actual = convertString2Dictionary(input)
            self.assertEqual(actual, expected)

