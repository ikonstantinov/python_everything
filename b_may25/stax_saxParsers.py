from xml.dom import pulldom
from xml import sax

print('''StAX''')
doc = pulldom.parse('tasks.xml')
print(doc)
for event, node in doc:
    if event == pulldom.START_ELEMENT and node.localName == 'task':
        doc.expandNode(node)
        print(node.firstChild.wholeText)

print('''\nSAX''')


class TaskHandler(sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.is_task = False

    def startElement(self, name, attrs):
        if name == 'task':
            self.is_task = True

    def endElement(self, name):
        if name == 'task':
            self.is_task = False

    def characters(self, content):
        if self.is_task:
            print(content)


parser = sax.make_parser()
parser.setContentHandler(TaskHandler())
parser.parse(open('tasks.xml', 'rt'))
