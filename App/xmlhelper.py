__author__ = 'andong'

from xml.etree.ElementTree import Element, SubElement, ElementTree

def write(dict):
    #f = open('../files/test.data','w',encoding='utf-8')
    #for k in dict.keys():
    #    f.write(k+dict[k]+'\n')
    #f.close()
    # 生成根节点
    root = Element('root')
    # 生成第一个子节点 head
    head = SubElement(root, 'head')
    # head 节点的子节点
    title = SubElement(head, 'title')
    title.text = dict['title']
    writer = SubElement(head, 'writer')
    writer.text = dict['writer']
    nation = SubElement(head, 'nation')
    nation.text = dict['nation']
    # 生成 root 的第二个子节点 body
    body = SubElement(root, 'body')
    # body 的内容
    print(dict['content'])
    body.text = dict['content']
    tree = ElementTree(root)
    tree.write(dict['title']+'.sDOC', encoding='utf-8')

#def read():
