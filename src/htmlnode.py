class HTMLNode:
    def __init__(self, tag= None, value= None, children= None, props= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        value_repr = self.value if self.value else "" 
        children_repr = "".join([repr(child) for child in self.children])
        return f'<{self.tag}{self.props_to_html()}>{children_repr}{value_repr}</{self.tag}>'

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props)


    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if not self.props:
            return ""
        the_output = "".join(f' {key}="{value}"' for key, value in self.props.items()) 
        return the_output 

