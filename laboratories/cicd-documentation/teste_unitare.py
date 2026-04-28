import unittest
from tree import Tree
from node import Node

class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(10)
        self.tree.add(5)
        self.tree.add(15)

    def test_find_existing_element(self):
        node = self.tree._find(5, self.tree.getRoot())
        
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 5)

    def test_find_non_existing_element(self):
        node = self.tree._find(100, self.tree.getRoot())
        
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()