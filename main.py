import os
def clear():
  print("\033c", end="")


URL = "https://blog.myfitnesspal.com/"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

clear()
print("Loading...")

driver.get(URL)

trending_articles = driver.find_element(By.CLASS_NAME, "module-trending")

trending_articles_list = trending_articles.find_element(By.TAG_NAME, "ul").find_element(By.CLASS_NAME, "slick-list").find_elements(By.CLASS_NAME, "slick-slide")

articles = [] # Each array object should have a Title with a url

for idx in range(len(trending_articles_list)):
  element = trending_articles_list[idx].find_element(By.CLASS_NAME, "module-trending-card-title") 
  title = element.get_property("text")
  url = element.get_property("href")
  articles.append([title, url])

driver.close()

def printArticle(idx):
  while True:
    clear()
    print(f"{articles[idx][0]}")
    print(f"URL: {articles[idx][1]}")
    goBack = input("Go back (Y for yes, N for no): ").lower()
    if goBack == "y":
      printArticles()
      break
    elif goBack == "n":
      break

def printArticles(rangeStart = 0, rangeEnd = 5):
  newRangeEnd = 0
  if rangeEnd > len(articles):
    newRangeEnd = len(articles)
  else:
    newRangeEnd = rangeEnd
  while True:
    clear()
    print("Trending Articles By My Fitness Pal: ")
    for idx in range(rangeStart, newRangeEnd):
      print(f"{str(idx+1)}. {articles[idx][0]}")
    option = input("Article Number (N for next 5, P for previous 5): ").lower()
    if option == "n" and newRangeEnd != len(articles):
      printArticles(rangeStart+5, rangeEnd+5)
      break
    elif option == "p" and rangeStart != 0:
      printArticles(rangeStart-5, rangeEnd-5) 
      break
    else:
      try:
        optionNum = int(option)
      except:
        printArticles(rangeStart, rangeEnd) 
        break
    if rangeStart <= optionNum - 1 < newRangeEnd:
      printArticle(optionNum - 1)
      break
    


printArticles()
clear()
print("Thank you")

