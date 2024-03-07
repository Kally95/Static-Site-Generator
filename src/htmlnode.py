class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        props_str = " "
        for attribute, value in self.props.items():
            props_str += f' {attribute}="{value}"'
        return props_str.strip()
    
    def __repr__(self):
        return f"{self.tag} {self.value} {self.children} {self.props}"