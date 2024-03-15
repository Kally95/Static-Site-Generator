class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_str = ""
        for attribute, value in self.props.items():
            props_str += f' {attribute}="{value}"'
        return props_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, children, props)

    def to_html(self):
            self_closing_tags = set(['area',
                'base',
                'br',
                'col', 
                'embed', 
                'hr', 
                'img', 
                'input', 
                'link', 
                'meta', 
                'param', 
                'source', 
                'track', 
                'wbr', 
            ])
            start_tag = f'<{self.tag}'
            closing_tag = f'</{self.tag}>'
            attr_str = ''
            if self.props != None:
                for attribute, value in self.props.items():
                    attr_str += f' {attribute}="{value}"'
            if self.tag in self_closing_tags:
                return start_tag + attr_str + '>'
            if self.value == None:
                raise ValueError
            if self.tag == None:
                return self.value
            return start_tag + attr_str +'>' + self.value + closing_tag
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
            print(children_html)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"