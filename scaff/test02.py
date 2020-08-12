# -*- coding: utf-8 -*-

"""
"""

about_str = """Using Brython to help the user to invent palindroms.
A looooong-dreamed-of little project.

José L Balcázar (balqui at GitHub), 2020"""

from browser import document, alert, html # Brython in-browser support

def about():
	alert(about_str)

def start(event):
	document["main"].value = "Placeholder text"
	document["refr"].disabled = False
	document["main"].disabled = False

def refresh(ev):
	print("Must refresh. Contents right now:")
	print(document["main"].value)


# main program: 
# bind buttons to processes and leave everything for Brython to care for.

document['about'].bind('click', about)

document['start'].bind('click', start)


