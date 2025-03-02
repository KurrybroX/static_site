from parentnode import *
from leafnode import *
import unittest

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",)
    def test_to_html_parents_in_parents(self):
        leaf_to_start = LeafNode("b", "grandchild")
        first_parent = ParentNode("span", [leaf_to_start]) 
        second_parent = ParentNode("div", [first_parent]) 
        third_parent = ParentNode("span", [second_parent])
        self.assertEqual(third_parent.to_html(), "<span><div><span><b>grandchild</b></span></div></span>",)
if __name__ == "__main__":
    unittest.main()
