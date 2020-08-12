"""
Test for the palindrom helper
Directly Python3
"""

import tkinter

class Test:

    @classmethod
    def __init__(cls):
        cls.root = tkinter.Tk()

        text_width = 92
        text_height = 28

        cls.console = tkinter.Text(cls.root)
        cls.console.configure(width = text_width, height = text_height)
        cls.console.pack(side=tkinter.LEFT)

        cls.end = tkinter.Button(cls.root)
        cls.end.configure(text = "Quit",
                          command = cls.root.destroy)
        cls.end.pack()

        cls.look = tkinter.Button(cls.root)
        cls.look.configure(text = "Look",
                          command = cls.look)
        cls.look.pack()

        cls.root.mainloop()

    @classmethod
    def look(cls):
        cls.console.insert(0, "Some initial text to start from.")
        print("Plan is to write here contents of text widget somehow")


if __name__ == "__main__":

    i = Test()
    # ~ i.console.insert(0, "Some initial text to start from.")

    # ~ i.console.see("end-2c")
