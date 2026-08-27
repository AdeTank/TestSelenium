import time
from selenium import webdriver

print("Starting...")

try:
    driver = webdriver.Chrome()
    print("Chrome driver started")

    driver.get("https://www.google.com")
    print("Page loaded, title:", driver.title)

    time.sleep(5)
    driver.quit()
    print("Done")

except Exception as e:
    print("ERROR:", e)