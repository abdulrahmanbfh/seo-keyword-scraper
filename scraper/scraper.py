import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
import pandas as pd

def scrape_google(query, max_results=10):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    service = Service(os.path.normpath('env/Lib/site-packages/msedgdriver/msedgedriver.exe'))
    driver = webdriver.Edge(service=service, options=options)

    try:
        url = f"https://www.google.com/search?q={query}"
        driver.get(url)
        time.sleep(3)  # Allow time for page to load

        results = []
        elements = driver.find_elements(By.CSS_SELECTOR, "h3")
        for element in elements[:max_results]:
            results.append(element.text)

        return pd.DataFrame({'Keyword': results})
    finally:
        driver.quit()