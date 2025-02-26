import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_params(self):
        node = TextNode("This is yet another text node", TextType.PLAIN, None)
        node2 = TextNode("This is yet another text node", TextType.PLAIN)
        self.assertEqual(node,node2)
    def test_mismatch(self):
        node = TextNode("This is another one", TextType.PLAIN, None)
        node2 = TextNode("This is another one", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)
if __name__ == "__main__":
    unittest.main()
