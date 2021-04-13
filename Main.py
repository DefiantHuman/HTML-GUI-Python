from tkinter import *
display_text = "Testing"
window = Tk()
window.title("HTML")
window.configure(width=800, height=800)
T = Text(window, height = 5, width = 52)
T.insert(END, display_text)
b1 = Button(window, text = "START")
T.pack()
b1.pack()
window.mainloop()