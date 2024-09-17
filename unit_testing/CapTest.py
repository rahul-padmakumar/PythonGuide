import unittest
from CapSample import capitalize_string


class CapTest(unittest.TestCase):

    def test_single_word(self):
        input_data = 'python'
        cap_input_data = capitalize_string(input_data)
        self.assertEquals(cap_input_data, 'Python')

    def test_multiple_word(self):
        input_data = 'jack sparrow'
        cap_input_data = capitalize_string(input_data)
        self.assertEquals(cap_input_data, 'Jack Sparrow')
