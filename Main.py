from tkinter import *
def Close():
    window.destroy()
display_text = "Welcome! This is a Python based html editor."
window = Tk()
window.title("HTML")
window.configure(width=800, height=800)
T = Text(window, height = 5, width = 52)
T.insert(END, display_text)
b1 = Button(window, text = "START")
b2 = Button(window, text = "EXIT", command=Close)
T["state"] = DISABLED
T.pack()
b1.pack()
b2.pack()
window.mainloop()