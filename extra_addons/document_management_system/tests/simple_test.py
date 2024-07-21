import unittest
from .. import models

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

print(models.document.Document._name)
print(models.employee.Employee._name)
print("I would test some more, if I could...")
# TestStringMethods.test_upper(models.document)
# TestStringMethods.test_upper(models.document)
# TestStringMethods.test_upper(models.document)