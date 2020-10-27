from selenium import webdriver
import pyautogui, time
import json
browser = webdriver.Firefox()
wordsArray = []
user = []
password = []
email = 'YOUREMAILHERE'
password = 'YOURPASSWORDHERE'
url1 = 'https://monkeytype.com/login'
url = 'https://monkeytype.com/'
browser.get(url1)
time.sleep(3)
browser.find_element_by_xpath("//input[@autocomplete='email']").send_keys(email)
browser.find_element_by_xpath("//input[@autocomplete='password']").send_keys(password)
clickLogin = browser.find_element_by_xpath("//i[@class='fas fa-sign-in-alt']")
clickLogin.click()
time.sleep(2)
browser.get(url)
time.sleep(2)
while True:
    firstWord = browser.find_elements_by_xpath("//div[@class='word active']")
    for i in firstWord:
        wordsArray.append(i.text)
    for word in wordsArray:
        pyautogui.typewrite(word)
        print(word)
        pyautogui.press("space")
        print(" ")
        firstWord.clear()
        wordsArray.clear()
