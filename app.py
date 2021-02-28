from selenium import webdriver

from pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path="/home/disciple/chromedriver")
chrome.get("http://quotes.toscrape.com")
page = QuotesPage(chrome)

for quote in page.quotes:
    print(quote)