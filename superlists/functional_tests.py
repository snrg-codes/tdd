from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://kun.uz/ru')

assert 'Все' in browser.title

