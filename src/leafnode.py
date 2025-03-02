from htmlnode import *

class LeafNode(HTMLNode):

    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children = [], props=props)
        if not value and not props:
            raise ValueError("LeafNode must have a value or props")
        self.value = value

    def to_html(self):
        if self.tag and not self.value:
            return f'<{self.tag}{self.props_to_html()} />'
        if self.tag:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        return self.value 

