from selenium import webdriver
import math
import time

# использование JS  чтобы прокрутить перекрытый элемент до видимости


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_css_selector('#input_value').text

    browser.find_element_by_css_selector("#answer").send_keys(calc(x))

    check = browser.find_element_by_css_selector("#robotCheckbox")
    check.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    radio = browser.find_element_by_css_selector("#robotsRule")
    radio.click()
    button.click()
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()