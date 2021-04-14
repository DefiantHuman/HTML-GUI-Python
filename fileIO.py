def Write(html):
  # opens index.html in write mode
  file = open("index.html", "w")
  # clears the file so that we can't add to the file
  file.truncate(0)
  # writes a little comment and the html to the file
  file.write("<!-- Written by Python program--> \r" + html)
  # closes the file
  file.close()

def Read():
  # reads file back and prints to Result
  file = open("index.html", "r")
  html_read = file.read()
  print("File contents: \r" + html_read)