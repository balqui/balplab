
from browser import document, alert # Brython in-browser support

about_str = """Using Brython to help the user to invent palindroms.
A looooong-dreamed-of little project.

José L Balcázar (balqui at GitHub), 2020"""

def about(ev):
    alert(about_str)

def refresh(ev):
    curr = document["work"].value
    for c in reversed(curr):
        curr += c
    document["work"].value = curr + curr
    
def where(ev):
	print("Clicked at clientX:", ev.clientX)

document["work"].bind('click', where)

# main program: 
# bind buttons to processes and leave everything for Brython to care for.

document['about'].bind('click', about)
document['refr'].bind('click', refresh)

# <script type="text/python" src="test02.py"></script>
