from unittest import TestCase
import dispatch as nav
# import lambda.dispatch as nav

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
        self.assertDictEqual(actual, expected)

