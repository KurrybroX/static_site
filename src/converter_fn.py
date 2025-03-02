from textnode import *
from leafnode import *

def text_node_to_html_node(textnode):
    match textnode.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=textnode.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=textnode.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=textnode.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=textnode.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=textnode.text, props={"href": textnode.url}).to_html()
        case TextType.IMAGE:
            return LeafNode(tag="img", value=None, props={"src": textnode.url, "alt":textnode.text}).to_html()
        case _:
            raise ValueError(f"Unsupported TextType: {textnode.text_type}")
