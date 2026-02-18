import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


def accept_cookies(driver):
    try:
        wait = WebDriverWait(driver, 5)
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Accept') or contains(., 'Aceptar')]"))
        )
        button.click()
    except:
        pass


def get_opinion_articles(driver):
    driver.get("https://elpais.com/opinion/")
    accept_cookies(driver)

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article h2 a"))
    )

    elements = driver.find_elements(By.CSS_SELECTOR, "article h2 a")

    urls = []
    for el in elements[:5]:
        href = el.get_attribute("href")
        if href:
            urls.append(href)

    return urls


def scrape_article(driver, index):
    wait = WebDriverWait(driver, 15)

    try:
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "article#main-content")
            )
        )

        # ---- TITLE ----
        try:
            title_element = driver.find_element(
                By.CSS_SELECTOR,
                "article#main-content h1"
            )
            title = title_element.text.strip()
        except:
            title = ""

        # ---- PRIMARY BODY SELECTOR ----
        paragraphs = driver.find_elements(
            By.CSS_SELECTOR,
            "article#main-content div[data-dtm-region='articulo_cuerpo'] p"
        )

        # ---- FALLBACK BODY SELECTOR ----
        if not paragraphs:
            paragraphs = driver.find_elements(
                By.CSS_SELECTOR,
                "article#main-content p"
            )

        content = "\n".join(
            [p.text for p in paragraphs if p.text.strip()]
        )

    except Exception as e:
        print("Error extracting article:", e)
        title = ""
        content = ""

    print("\n----------------------------")
    print("Title (Spanish):", title)
    print("Content (Spanish):", content[:500], "...")

    # ---- IMAGE ----
    try:
        img = driver.find_element(
            By.CSS_SELECTOR,
            "article#main-content figure img"
        )
        img_url = img.get_attribute("src")

        if img_url:
            if not os.path.exists("images"):
                os.makedirs("images")

            img_data = requests.get(img_url).content
            with open(f"images/article_{index}.jpg", "wb") as f:
                f.write(img_data)

            print("Image downloaded.")
    except:
        print("No image found.")

    return title




    return title
