from tkinter import *
def Close_start():
    start.destroy()
def Close_main():
    main.destroy()
def Main_win():
    global main
    Close_start()
    main = Tk()
    main.title("HTML Editor")
    main.geometry("1000x700")
    display_text = "HTML Editor"
    T = Text(main, height = 2, width = 15)
    T.insert(END, display_text)
    T["state"] = DISABLED
    T.pack()
    TITLE = Text(main, height = 2, width = 20)
    TITLE.insert(END, "Title: ")
    TITLE["state"] = DISABLED
    TITLE.place(x=30, y=40)
    title = Entry(main, width=13, font=("Arial", 12))
    title.place(x=210, y=46)
    HEADING = Text(main, height = 2, width = 20)
    HEADING.insert(END, "Heading: ")
    HEADING["state"] = DISABLED
    HEADING.place(x=30, y=80)
    heading = Entry(main, width=13, font=("Arial", 12))
    heading.place(x=210, y=86)
    BODY = Text(main, height = 2, width = 20)
    BODY.insert(END, "Body: ")
    BODY["state"] = DISABLED
    BODY.place(x=30, y=120)
    body = Entry(main, width=13, font=("Arial", 12))
    body.place(x=210, y=126)
    Exit = Button(main, text = "EXIT", command=Close_main).place(x=880, y=300)
    main.mainloop()
def Main():
    global start
    display_text = "Welcome! This is a Python based html editor. \nTo begin press START."
    start = Tk()
    start.title("HTML") 
    start.configure(width=800, height=800)
    T = Text(start, height = 5, width = 52)
    T.insert(END, display_text)
    b1 = Button(start, text = "START", command=Main_win)
    b2 = Button(start, text = "EXIT", command=Close_start)
    T["state"] = DISABLED
    T.pack()
    b1.pack()
    b2.pack()
    start.mainloop()
Main()