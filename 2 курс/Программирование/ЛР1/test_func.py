import unittest
from main import gen_bin_tree

class TestStringMethods(unittest.TestCase):
    def test_bin_tree(self):
        self.assertEqual(gen_bin_tree(height=1, root=1), {'1': []})
        self.assertEqual(gen_bin_tree(height=1, root=5).get('5'), [])

unittest.main(verbosity=1)