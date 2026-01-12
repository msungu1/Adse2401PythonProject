# python script to demonstrate opening the Python official site
# and searching for a term ('lists') on the site

# NB: ensure selenium is installed: pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set up the browser (Safari or Firefox)
driver = webdriver.Firefox()   # requires geckodriver installed

# create an explicit wait object (wait up to 20 seconds)
wait = WebDriverWait(driver, 20)

# open the official Python website
driver.get("https://www.python.org")

# wait for the search box to be present and interactable
search_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "q"))
)

# enter our search term 'lists' and submit
search_box.send_keys("lists")
search_box.send_keys(Keys.RETURN)

# optional: wait for results page to load and print title
wait.until(EC.title_contains("lists"))
print("Page title after search:", driver.title)

# close the browser
driver.quit()
