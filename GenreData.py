from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import operator
kill = False
driver = webdriver.Firefox()
while kill == False:
    gamesToCheck = int(input("How many games to check?\n"))
    pageToCheck = input("Which page would you like to view? (i.e: games, games/platform-web, etc.)\n")
    driver.get(f"https://itch.io/{pageToCheck}")
    i = 0
    GameData = {}
    FinalData = []
    for x in range(round(gamesToCheck/10) + 8):
        
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
    for genre in driver.find_elements(By.CLASS_NAME, "game_genre"):
        if i < int(gamesToCheck):
            i += 1
        else:
            break
        if not genre.text in GameData.keys():
            GameData[genre.text] =1
        else:
            GameData[genre.text]+=1
    print(f"The Statistics for the current top {gamesToCheck} entries in {pageToCheck} are:")
    sorted_d = dict(sorted(GameData.items(), key=operator.itemgetter(1),reverse=True))
    for key in sorted_d.keys():
        FinalData.append(f"|  {key}: {round((sorted_d[key]/gamesToCheck)*100,2)}% ({sorted_d[key]} games)")
    for i in FinalData:
        print(i)
    DoKill = input("Find some more data? (y/n)\n")
    if DoKill != 'y':
        kill = True 
