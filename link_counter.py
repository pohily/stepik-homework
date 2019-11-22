""" Поиск всех неработающих ссылок на странице """
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
site = 'https://mail.ru'
try:
    browser.get(site)
    elements = browser.find_elements(By.TAG_NAME, "a")
    links, fails = [], []
    for element in elements:
        links.append(element.get_attribute('href'))
    print(len(links))
    for index, link in enumerate(links):
        try:
            code = urlopen(link).getcode()
            # На бою надо раскомментировать sleep, чтобы тест не приняли за dos атаку
            print(index, link, code)
            time.sleep(0.5)
            if code != 200:
                fails.append((index, elements[index].get_attribute('text'), link))
        except Exception:
            if link.startswith('mailto:') or link.startswith('tel:'):
                continue
            fails.append((index, elements[index].get_attribute('text'), link))
    print(f'\n\nНа странице {site} не открывается {len(fails)} ссылка/и/ок из {len(links)}')
    print('Номер ссылки\tТекст ссылки\t\tСсылка')
    print('----------------------------------------------------')
    for fail in fails:
        print(fail)
finally:
    browser.quit()
