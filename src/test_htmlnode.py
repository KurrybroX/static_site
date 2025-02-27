from htmlnode import *

import unittest

class TestHTMLNode(unittest.TestCase):
    def test_default(self):
        node = HTMLNode()
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node, node2)
    def test_tag(self):
        node = HTMLNode("p")
        node2 = HTMLNode("p",None, None, None)
        self.assertEqual(node, node2)
        node3 = HTMLNode("h1")
        node4 = HTMLNode("a")
        self.assertNotEqual(node3, node4)
    def test_value(self):
        node = HTMLNode(None, "blah blah blah")
        node2 = HTMLNode(None, "ya ya ya")
        self.assertNotEqual(node, node2)    
if __name__ == "__main__":
    unittest.main()
