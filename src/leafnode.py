from htmlnode import *

class LeafNode(HTMLNode):

    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, props, children = [])
        if not value:
            raise ValueError("LeafNode must have a value")
        self.value = value
