from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element_by_css_selector('#num1').text)
    num2 = int(browser.find_element_by_css_selector('#num2').text)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(num1 + num2))

    submit = browser.find_element_by_css_selector("button")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()