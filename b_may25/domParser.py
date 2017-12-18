from xml.dom import minidom

tree = minidom.parse('tasks.xml')
# print(dir(tree))
print(tree.firstChild.firstChild)
for el in tree.firstChild.firstChild.childNodes:
    print(el.firstChild.wholeText)