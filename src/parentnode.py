from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        

    def to_html(self):
        if not self.children:
            raise ValueError("ParentNode must have children")
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        return f'<{self.tag}{self.props_to_html()}>{"".join(child.to_html() for child in self.children)}</{self.tag}>'
