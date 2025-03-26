class HTMLNode: 
    def __init__(self, tag:str = None , value:str = None, children:list = None, props:dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self): 
        raise NotImplementedError
    
    def props_to_html(self): 
        prop_string = ""
        for prop in self.props:
            prop_string = prop_string + f'{prop}="{self.props[prop]}"'
        
        return prop_string
    
    def __repr__(self):
        class_name = type(self).__name__
        return f"""{class_name}
                    tag: {self.tag}
                    value: {self.value}
                    children: {self.children}
                    props: {self.props}"""




        