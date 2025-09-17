import unittest
from src.app.main import process_data

class TestApp(unittest.TestCase):
    def test_process_data_correct_input(self):
        # A test case to ensure the function works with correct input.
        self.assertEqual(process_data(50), 150)

    def test_process_data_buggy_input(self):
        # This test is designed to fail, exposing the bug.
        with self.assertRaises(TypeError):
            process_data("50")

if __name__ == "__main__":
    unittest.main()
