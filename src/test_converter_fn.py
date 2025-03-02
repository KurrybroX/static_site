from converter_fn import *
from textnode import *
import unittest

class TestTextNodeToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node") 
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(str(html_node),'<a href="www.google.com">This is a link node</a>')       
    def test_img(self):
        node = TextNode("This is a image node", TextType.IMAGE, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node,'<img src="www.google.com" alt="This is a image node" />')
if __name__ == "__main__":
    unittest.main()
