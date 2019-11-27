from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_css_selector('#treasure')
    x = treasure.get_attribute('valuex')
    y = calc(x)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    check = browser.find_element_by_css_selector("#robotCheckbox")
    check.click()
    radio = browser.find_element_by_css_selector("#robotsRule")
    radio.click()
    submit = browser.find_element_by_css_selector("button")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()