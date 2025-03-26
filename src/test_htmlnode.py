import unittest
from htmlnode import HTMLNode

class testHtmlNode(unittest.TestCase): 
    def test_ensure_none(self):
        p_node = HTMLNode("<p>", "This is text for a htmlnode")
        self.assertEqual(p_node.props, None)
        self.assertEqual(p_node.children, None)

    def test_check_props(self): 
        prop_item = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        p_node = HTMLNode("<p>", "This is text for a htmlnode", children=None,props=prop_item)
       
        self.assertIn("target", p_node.props)

    def test_print_htmlnode(self): 
        p_node = HTMLNode("<p>", "This is text for a htmlnode")

        self.assertEqual(type(None),type(print(p_node)))