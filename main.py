from scraper import setup_driver, get_opinion_articles, scrape_article
from translator import translate_title
from analyzer import analyze_titles


def main():
    driver = setup_driver()

    article_urls = get_opinion_articles(driver)

    translated_titles = []

    for i, url in enumerate(article_urls):

        driver.get(url)

        title = scrape_article(driver, i)

        translated = translate_title(title)
        translated_titles.append(translated)

    analyze_titles(translated_titles)

    driver.quit()


if __name__ == "__main__":
    main()
