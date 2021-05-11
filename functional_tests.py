from selenium import webdriver


if __name__ == '__main__':
    browser = webdriver.Chrome("chromedriver")
    browser.get("http://localhost:8000")

assert 'worked successfully' in browser.title