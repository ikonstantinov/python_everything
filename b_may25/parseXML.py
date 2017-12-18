"""
3 types of parsers:
 DOM - для небольших файлов, так как файл выгружается в память и индексируется - для многократного обращения к файлу
 StAX - потоковый парсер
 SAX - потоковый парсер
 
 StAX/SAX - если ошибка в документе - данные возвращаются, ДОМ - не возвращает
"""


from xml.etree import ElementTree as et
root = et.Element('tasks')
day = et.SubElement(root, 'day')
day.set('date', '01.01.2018')

task1 = et.SubElement(day, 'task')
task1.text = 'Wake up'

task2 = et.SubElement(day, 'task')
task2.text = 'Make coffee!'

tree = et.ElementTree(root)
tree.write('tasks.xml')

'''parse doc'''
tree2 = et.parse('tasks.xml')
print(tree2.findall("day[@date='01.01.2018']//task"))