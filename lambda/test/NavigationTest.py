from unittest import TestCase
from .. import dispatch as nav

class NavigationTest(TestCase):
    def shouldReturnErrorIfAltitudeExists(self):
        input = {
            'altitude': 'something'
        }
        expected = {
            'altitude': 'something',
            'error': 'altitude already exists in the input'
        }
        actual = nav.adjust(input)
        return self.assertDictEqual(actual, expected)

