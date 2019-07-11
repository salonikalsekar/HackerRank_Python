# Sample Input
#
# 6
# <feed xml:lang='en'>
#     <title>HackerRank</title>
#     <subtitle lang='en'>Programming challenges</subtitle>
#     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#     <updated>2013-12-25T12:00:00</updated>
# </feed>
# Sample Output
#
# 5
# Explanation
#
# The feed and subtitle tag have one attribute each - lang.
# The title and updated tags have no attributes.
# The link tag has three attributes - rel, type and href.
#
# So, the total score is 1+1+0+3

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
        return len(node.attrib) + sum(get_attr_number(child) for child in node)


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))