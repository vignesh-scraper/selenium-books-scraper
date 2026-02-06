from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def scrape_books():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://books.toscrape.com/")

    titles = []

    while True:
        books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod h3 a")

        for book in books:
            titles.append(book.get_attribute("title"))

        print("page completed...")

        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
            next_button.click()
            time.sleep(2)
        except:
            break

    driver.quit()
    print("Total books scraped:", len(titles))


if __name__ == "__main__":
    scrape_books()
