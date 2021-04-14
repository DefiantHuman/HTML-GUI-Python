import webbrowser as web
import os
def close():
    i = input("Close browser? ")
    if(i == "Yes"):
        os.system("TASKKILL /F /IM " + "firefox" +".exe")
    elif(i == "Y"):
        os.system("TASKKILL /F /IM " + "firefox" +".exe")
    elif(i == "yes"):
        os.system("TASKKILL /F /IM " + "firefox" +".exe")
    elif(i == "y"):
        os.system("TASKKILL /F /IM " + "firefox" +".exe")
def browser(i):
    if(i == "Yes"):
        web.open_new("index.html")
        close()
    elif(i == "Y"):
        web.open_new("index.html")
        close()
    elif(i == "yes"):
        web.open_new("index.html")
        close()
    elif(i == "y"):
        web.open_new("index.html")
        close()