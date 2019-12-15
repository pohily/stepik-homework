from selenium import webdriver
import math
import time

# переход на другую вкладку


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.find_element_by_css_selector('button').click()
    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_css_selector('#input_value').text
    browser.find_element_by_css_selector("#answer").send_keys(calc(x))
    button = browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()