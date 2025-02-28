from leafnode import *

import unittest

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    def test_leaf_href(self):
        node = LeafNode("a","Click me!", {"href": "https://www.google.com"})
        print(node.to_html())
        print(f"this is props: {node.props}")
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
if __name__ == "__main__":
    unittest.main()
