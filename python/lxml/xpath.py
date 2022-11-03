import io

from lxml import etree


sio = io.StringIO("""
<a>
 <b>
 </b>
</a>
""")
tree = etree.parse(sio)
node = tree.xpath("/a")[0]
node2 = node.xpath("b")
print(node2)
