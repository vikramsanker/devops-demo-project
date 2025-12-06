from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
assert "Google" in driver.title
driver.quit()
print("Selenium test passed!")
