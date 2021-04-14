from tkinter import *
import fileIO
# used to close the windows
def Close_start():
    start.destroy()
def Close_main():
    main.destroy()
# writes html code to a file
def Write(html):
  # opens index.html in write mode
  file = open("index.html", "w")
  # clears the file so that we can't add to the file
  file.truncate(0)
  # writes a little comment and the html to the file
  file.write("<!-- Written by Python program--> \r" + html)
  # closes the file
  file.close()
# Main Editing Window
def Main_win():
# sets variables to global so they can be accessed in another function
    global main, title, heading, body
    Close_start()
    main = Tk()
    main.title("HTML Editor")
    main.geometry("1000x700")
    display_text = "HTML Editor"
    T = Text(main, height = 2, width = 15)
    T.insert(END, display_text)
    T["state"] = DISABLED
    T.pack()
    directions= "Fill boxes then press CREATE to see your webpage."
    I = Text(main, height=2)
    I.insert(END, directions)
    I["state"] = DISABLED
    I.pack()
    TITLE = Text(main, height = 2, width = 10)
    TITLE.insert(END, "Title: ")
    TITLE["state"] = DISABLED
    TITLE.place(x=30, y=80)
    title = Entry(main, width=30, font=("Arial", 12))
    title.place(x=150, y=86)
    HEADING = Text(main, height = 2, width = 10)
    HEADING.insert(END, "Heading: ")
    HEADING["state"] = DISABLED
    HEADING.place(x=30, y=120)
    heading = Entry(main, width=30, font=("Arial", 12))
    heading.place(x=150, y=126)
    BODY = Text(main, height = 2, width = 10)
    BODY.insert(END, "Body: ")
    BODY["state"] = DISABLED
    BODY.place(x=30, y=160)
    body = Text(main, width=30, height=6, font=("Arial", 12))
    body.place(x=150, y=166)
    Exit = Button(main, text = "EXIT", command=Close_main, height=6, width=12,  bg="red", activebackground='gray').place(x=880, y=575)
    Create = Button(main, text= "CREATE", command=CREATE, height=6, width=30, bg="green", activebackground='gray').place(x=650, y=130)
    main.mainloop()
def Main():
# sets start to global so that it can be used by the close functions to destroy it
    global start
    display_text = "Welcome! This is a Python based html editor. \nTo begin press START."
    start = Tk()
    start.title("HTML") 
    start.geometry("500x500")
    T = Text(start, height = 5, width = 52)
    T.insert(END, display_text)
    b1 = Button(start, text = "START", command=Main_win)
    b2 = Button(start, text = "EXIT", command=Close_start)
    T["state"] = DISABLED
    T.pack()
    b1.pack()
    b2.pack()
    start.mainloop()
# called when user hits the create button
# makes html code then calls a function to write it to a file
def CREATE():
    HTML_title=title.get()
    HTML_head=heading.get()
    HTML_body=body.get(1.0, "end-1c")
    HTML= "<html>\n<head>\n<title>" + HTML_title + "</title></head>\n<body>\n<h2>" + HTML_head +"</h2>\n<p>"+ HTML_body
    HTML = HTML + "</p></body>\n</html>"
    Write(HTML)
Main()