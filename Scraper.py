from selenium import webdriver
from bs4 import BeautifulSoup
from threading import Thread
from urllib.request import urlopen 

def function(): 
    driver = webdriver.Chrome(r"C:\Users\maini\Downloads\chromedriver.exe")
    protocols = driver.get("https://app.cleartriage.com/app/#/protocols")

    # Requires a second URL because the website requires a sign-in, and the URL changes after the sign-in
    protocols2 = input("url: ")
    html = urlopen(protocols2).read()
    soup = BeautifulSoup(html, features="html.parser")    
    
    #kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    
        # get text
        text = soup.get_text()
    
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
    
        print(text)
        
function()

#increase wesbite timeout to give enough time to complete sign-in
action_thread = Thread(target=function)
action_thread.start()
action_thread.join(timeout=15)
