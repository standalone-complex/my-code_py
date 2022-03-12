from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.baidu.com')
print(browser.current_url)
