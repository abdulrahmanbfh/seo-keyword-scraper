import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
import pandas as pd
from urllib.parse import urlparse

def scrape_google(query, max_results=100):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    service = Service(os.path.normpath('env/Lib/site-packages/msedgdriver/msedgedriver.exe'))
    driver = webdriver.Edge(service=service, options=options)

    try:
        overall_position = 0
        results = []
        for i in range(0, max_results, 10):
            url = f"https://www.bing.com/search?q={query}&rdr=1&first={i+1}"
            driver.get(url)
            time.sleep(3)  # Allow time for the page to load

            #search_results = driver.find_elements(By.CSS_SELECTOR, ".b_algo[class='b_algo']")  # Google search result container
            search_results = driver.find_elements(By.CSS_SELECTOR, ".b_algo , .b_ad")  # Google search result container

            for position, result in enumerate(search_results[:max_results], start=1):
                overall_position = overall_position + 1
                try:
                    # Extract title
                    title = result.find_element(By.CSS_SELECTOR, "[h^='ID=SERP,']").text

                    # Extract URL
                    url = result.find_element(By.CSS_SELECTOR, "cite").text

                    # Extract domain
                    domain = urlparse(url).netloc

                    # Extract text (snippet/description)
                    try:
                        text = result.find_element(By.CSS_SELECTOR, "[class^='b_lineclamp']").text
                    except Exception as e:
                        text = "N/A"

                    # Extract date (if available)
                    try:
                        date = result.find_element(By.CSS_SELECTOR, "span.news_dt").text
                    except Exception as e:
                        date = "N/A"

                    # Add details to results
                    results.append({
                        "Keyword": query,
                        "Position": overall_position,
                        "Title": title,
                        "Text": text,
                        "Date": date,
                        "Domain": domain,
                        "URL": url
                    })
                except Exception as e:
                    # Handle cases where elements may not be present
                    print(f"Error scraping result at position {position}: {e}")

        return pd.DataFrame(results)
    finally:
        driver.quit()