import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):

    def test_props_to_html(self):
        node_w_whitespace = HTMLNode(tag='a', value='Click me', props={'href': 'https://www.example.com', 'target': '_blank'})

        self.assertEqual(' href="https://www.example.com" target="_blank"', node_w_whitespace.props_to_html()
        )

if __name__ == "__main__":
    unittest.main()
