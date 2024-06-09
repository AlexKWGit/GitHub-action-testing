import unittest
from unittest.mock import patch
import io
import sys
from Name_city import name_city_program

def get_output(func, inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func(*inputs)
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()

class TestNameCityProgram(unittest.TestCase):

    @patch('builtins.input', side_effect=['John', 'New York'])
    def test_name_city_program(self, mock_input):
        output = get_output(name_city_program, [])
        self.assertEqual(output.strip(), 'You name is John. You city is New York')

if __name__ == '__main__':
    unittest.main()
