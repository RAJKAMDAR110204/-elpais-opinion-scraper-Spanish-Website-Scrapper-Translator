from selenium import webdriver
from scraper import get_opinion_articles, scrape_article
from translator import translate_title
from analyzer import analyze_titles


def setup_driver():
    USERNAME = "rajkamdar_oItfYU"
    ACCESS_KEY = "njUQPzrRu1pDLLRH61ty"

    options = webdriver.ChromeOptions()

    options.set_capability("browserName", "Chrome")
    options.set_capability("browserVersion", "latest")

    options.set_capability("bstack:options", {
        "os": "Windows",
        "osVersion": "11",
        "buildName": "ElPais Automation Build",
        "sessionName": "ElPais Opinion Scraper Assignment"
    })

    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    return driver



def main():
    driver = setup_driver()

    try:
        article_urls = get_opinion_articles(driver)
        translated_titles = []

        for i, url in enumerate(article_urls):
            driver.get(url)

            title = scrape_article(driver, i)

            translated = translate_title(title)
            translated_titles.append(translated)

        analyze_titles(translated_titles)

        # Mark session as PASSED in BrowserStack
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", '
            '"arguments": {"status":"passed","reason": "ElPais scraper executed successfully"}}'
        )

    except Exception as e:
        # Mark session as FAILED in BrowserStack
        driver.execute_script(
            f'browserstack_executor: {{"action": "setSessionStatus", '
            f'"arguments": {{"status":"failed","reason": "{str(e)}"}}}}'
        )
        raise e

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
