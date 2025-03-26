from textnode import TextType
from textnode import TextNode

print("hello world")


def main():
    node = TextNode("This is some anchor text", TextType.BOLD, "https://facebook.com")
    print(node)


main()
