from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

url = "https://www.wikipedia.org/"
driver.get(url)
search_bar = driver.find_element(By.ID, "searchInput")
# Typing on searchbar
search_bar.send_keys("python programming")
icon_button = driver.find_element(By.CSS_SELECTOR, ".pure-button .svg-search-icon")
search_bar.send_keys(Keys.ENTER)
# icon_button.click()

# url = "https://www.python.org/"
# driver.get(url)
# python_docs = driver.find_element(By.LINK_TEXT, "Docs")
# Clicking an anchor tag/button
# python_docs.click()

# driver.quit()
