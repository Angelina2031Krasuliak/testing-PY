import unittest
from main import list_to_set


class TestListToSet(unittest.TestCase):

    def test_duplicates_removed(self):
        data = [1, 2, 2, 3, 4, 4, 5]
        result = list_to_set(data)
        self.assertEqual(result, {1, 2, 3, 4, 5})

    def test_return_type_is_set(self):
        data = [1, 1, 1]
        result = list_to_set(data)
        self.assertIsInstance(result, set)

if __name__ == "__main__":
    unittest.main()
