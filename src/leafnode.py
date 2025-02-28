from htmlnode import *

class LeafNode(HTMLNode):

    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children = [], props=props)
        if not value:
            raise ValueError("LeafNode must have a value")
        self.value = value

    def to_html(self):
        if not self.value:
            raise ValueError("LeafeNode must have a value")
        if not self.tag:
           return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

