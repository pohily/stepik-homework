import unittest
import time
from selenium import webdriver

""" Просто пример работы Unittest """


class TestAbs(unittest.TestCase):
    def test_register_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        first_name = browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']")
        first_name.send_keys('Michael')
        last_name = browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']")
        last_name.send_keys('Jackson')
        email = browser.find_element_by_xpath("//input[@placeholder = 'Input your email']")
        email.send_keys('1@google.com')
        # Отправляем заполненную
        time.sleep(2)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text, "Wrong text")

    def test_register_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        first_name = browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']")
        first_name.send_keys('Michael')
        last_name = browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']")
        last_name.send_keys('Jackson')
        email = browser.find_element_by_xpath("//input[@placeholder = 'Input your email']")
        email.send_keys('1@google.com')
        # Отправляем заполненную
        time.sleep(2)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text, "Wrong text")


if __name__ == "__main__":
    unittest.main()
