from selenium import webdriver
import os
import time

# использование os для загрузки файла

browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Michael")
    browser.find_element_by_name("lastname").send_keys("Jackson")
    browser.find_element_by_name("email").send_keys("mj@gmail.com")

    # file upload
    current_dir = os.getcwd() # либо path.abspath(os.path.dirname(__file__))
    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '2.2.8.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_name("file").send_keys(file_path)

    browser.find_element_by_css_selector("button").click()
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()