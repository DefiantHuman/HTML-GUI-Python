import fileIO
import browser as web

#element variables
title = input("Title: ")
heading = input("Heading: ")
body = input("Body: ")
style = input("Style: ")

html = "<html> "
html = html + "<head> <title>" + title + "</title><style>" + style + "</style></head> \r"
html = html + "<body> <h2>" + heading +"</h2> <p>" + body +"</p> \r"

fileIO.Write(html)

# tells user that it was saved
print("\r Code saved to index.html \r")

i = input("Print file?")
if(i == "Yes"):
  fileIO.Read()
elif(i == "Y"):
  fileIO.Read()
elif(i == "yes"):
  fileIO.Read()
elif(i == "y"):
  fileIO.Read()
i = input("Open HTML in browser? ")
web.browser(i)
print("\rCompleted")