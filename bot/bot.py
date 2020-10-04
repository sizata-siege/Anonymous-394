from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

username = "best_bot_selen"
password = "ez123456"
# wakasak596@treeheir.com

browser = webdriver.Chrome('./drivers/chromedriver.exe')

print('waiting 10 seconds ... ')
browser.implicitly_wait(10)

browser.get('https://www.instagram.com/')

username_xpath = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input"
password_xpath = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input"
login_btn_xpath = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button"

browser.find_element_by_xpath(username_xpath).send_keys(username)
browser.find_element_by_xpath(password_xpath).send_keys(password)
browser.find_element_by_xpath(login_btn_xpath).click()


print('waiting 10 seconds ... ')
sleep(5)


browser.get("https://www.instagram.com/progmage/")


posts_regex = "//a[contains(@href, '/p/')]"
arr = []
posts = browser.find_elements_by_xpath(posts_regex)
posts[3].click()

submit_btn_xpath = "/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button"

sleep(3)

textarea = browser.find_element_by_class_name(u"Ypffh")
submit_btn = browser.find_element_by_xpath(submit_btn_xpath)
print(submit_btn)
actions = ActionChains(browser)
actions.move_to_element(textarea)
actions.click()  # maybe not needed
actions.send_keys("BRRUUUUUH")
actions.move_to_element(submit_btn)
actions.click()
actions.perform()


# article
# 	div "EVERYTHING"
# 		div "EVERYTHING"
# 			div "ROW"
# 				div "ONE POST"
# 					a "CLICK ON THIS"
# 				div "ONE POST"
# 					a "CLICK ON THIS"
# 				div "ONE POST"
# 					a "CLICK ON THIS"
# 			div "ROW"
# 				div "ONE POST"
# 					a "CLICK ON THIS"
# 				div "ONE POST"
# 					a "CLICK ON THIS"
# 				div "ONE POST"
# 					a "CLICK ON THIS"

# browser.close()

# functions

# ============== CLASSES ============== #
# user
# page
# post
##
