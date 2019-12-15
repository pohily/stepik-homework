from selenium import webdriver
import math
import time

# модальные окна


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    browser.find_element_by_css_selector('button').click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_css_selector('#input_value').text
    browser.find_element_by_css_selector("#answer").send_keys(calc(x))
    button = browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()