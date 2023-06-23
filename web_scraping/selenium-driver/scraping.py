from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
url = "https://www.amazon.com/Apple-MacBook-Laptop-12%E2%80%91core-30%E2%80%91core/dp/B0BSHFCF13/ref=sr_1_3?keywords" \
      "=macbook+pro+2022+laptop&sr=8-3"
driver.get(url)
product = driver.find_element(By.ID, "productTitle")
print(product.text)
price = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]')
print(price.text)
amazon_search_bar = driver.find_element(By.NAME, "field-keywords")
print(amazon_search_bar.get_attribute("placeholder"))
amazon_logo = driver.find_element(By.CLASS_NAME, "nav-logo-link")
print(amazon_logo.size)
hamburger_menu = driver.find_element(By.CSS_SELECTOR, "#nav-main .nav-left #nav-hamburger-menu")
print(hamburger_menu.text)

headphone = driver.find_element(By.XPATH, '//*[@id="5Q38P0NJ"]/div/div/div/div/img')
print(headphone.get_attribute("alt"))
url = "https://www.python.org/"
driver.get(url)
upcoming_python_events = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu a")
events_calendar = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu time")

events = []
for i in range(len(events_calendar)):
    events.append({"number": i + 1, "date": events_calendar[i].text, "event": upcoming_python_events[i].text})

# Writing csv file
field_names = list(events[0].keys())
with open('upcoming_events.csv', 'w', encoding='UTF8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(events)

# driver.close()
