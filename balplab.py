# ~ <script type="text/python">
from browser import document, alert # Brython in-browser support
from store import Store

about_str = """BalPLab:

Using Brython to help the user to invent palindroms.
A looooong-dreamed-of little project.

Currently on Brython-3.8.9.

José L Balcázar (balqui at GitHub), summer 2020"""

# ~ arrow_codes = list(range(37, 41))
# ~ moves with <, > symbols; at keypress, < is 60 and > is 62
# ~ recall del is 8

st = Store()

def about(ev):
    alert(about_str)

def back(ev):
    alert("Back not yet implemented. Sorry.")

def done(ev):
    alert(st.writ(False))

def handlekey(ev):
    """Handle keypress event; earlier versions used
    keydown events to grab the arrows but then other
    things were grabbed in the meantime like caps or
    tildes. By the way, tildes are as yet unsolved.
    """
    # ~ alert(str(ev.keyCode) + " at handle key by keypress")
    if ev.keyCode == 61: 
        "did not manage to use the DEL key"
        st.delete()
        document["out"].value = st.writ()
        document["in"].value = ''
    elif ev.keyCode == 60: 
        st.move(-1)
        document["out"].value = st.writ()
        document["in"].value = ''
    elif ev.keyCode == 62: 
        st.move(1)
        document["out"].value = st.writ()
        document["in"].value = ''
    else:
        st.put(chr(ev.keyCode))
        document["out"].value = st.writ()
        document["in"].value = ''

# ~ def handlemove(ev):
    # ~ "handle move event"
    # ~ alert(str(ev.keyCode) + " at handle move by keydown")
    # ~ if ev.keyCode == 8:
        # ~ alert("Deletion unsupported as yet.")
    # ~ elif ev.keyCode in arrow_codes:
        # ~ "wrong here, must transform into distance to update"
        # ~ r = st.move(ev.keyCode)
        # ~ alert("moving: " + str(ev.keyCode) + ", " + r)
    # ~ else:
        # ~ alert("keydown ignored")
    
def mouseused(ev):
    alert("Don't use the mouse please.")
    document["in"].focus()

# main program: 
# bind buttons to processes and leave interaction for Brython to care for.

document["in"].bind('click', mouseused)
document["name"].bind('click', mouseused)
document["info"].bind('click', mouseused)
# ~ document["mo_s"].bind('click', mouseused)
# ~ document["mo_i"].bind('click', mouseused)
document["out"].bind('click', mouseused)
document["ignore"].bind('click', mouseused)
document["in"].bind('keypress', handlekey)
document['about'].bind('click', about)
# ~ document['back'].bind('click', back)
document['done'].bind('click', done)
# ~ </script>

