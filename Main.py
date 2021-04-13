from tkinter import *
display_text = "Welcome! This is a Python based html editor."
window = Tk()
window.title("HTML")
window.configure(width=800, height=800)
T = Text(window, height = 5, width = 52)
T.insert(END, display_text)
b1 = Button(window, text = "START")
T["state"] = DISABLED
T.pack()
b1.pack()
window.mainloop()