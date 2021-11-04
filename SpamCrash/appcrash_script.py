import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Atom Toolkit  - Virus Projection")
        #setting window size
        width=464
        height=191
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_835=tk.Message(root)
        ft = tkFont.Font(family='Times',size=13)
        GMessage_835["font"] = ft
        GMessage_835["fg"] = "#333333"
        GMessage_835["justify"] = "center"
        GMessage_835["text"] = "You have been infected by Atom SpamCrash Toolkit. Damn next time dont open random files :)"
        GMessage_835.place(x=90,y=10,width=298,height=153)
while True:
    if __name__ == "__main__":
        root = tk.Tk()
        app = App(root)
        root.mainloop()
