""""Useful functions"""''

'''Randoms words'''
# .join(random.choice(string.ascii_letters) for i in range(12)) - функция для вывода рандомного набора символов
# длиною 12 символов в string.ascii_letters так же доступны ascii_uppercase, ascii_lowercase

'''Random number'''
# (random.randint(1, 99)) - генерация чисел в диапазоне от 1 до 99

"""random symbols"""
# rnd_title = f" 1111aa {''.join(random.choice(string.ascii_letters) for i in range(5))}  provider0 "

# проверка создания языка, провайдера (с проверкой того, что после создания языка к примеру он есть в раскрывном
# списке создания демки) Проверить наличие не повторяющихся айди на странице Проверка фильтра


'''Проверка ссылок на статус код'''
# import requests
# from http import HTTPStatus as StatusCodes
#
# links = [
#     "https://stage-tody.sptech.team/",
#     "https://stage-tody.sptech.team/provider/list",
#     "https://stage-tody.sptech.team/tag/list/",
#     "https://stage-tody.sptech.team/language/list",
#     "https://stage-tody.sptech.team/users/list",
#     "https://stage-tody.sptech.team/demo/48/edit"
# ]
#
#
# def configure_pages_in_domain():
#     for link in links:
#         print(link)
#         response = requests.get(link, timeout=20)
#         if not response.status_code == StatusCodes.OK:
#             return print(f"error code: {response.status_code} {link}")
#         else:
#             print(f'All is OK)), status code is: {response.status_code}\n')
#
#
# configure_pages_in_domain()

import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

# class TestStartPage:
#
#     def random_num(self):
#         """Generate random number"""
#         return str(random.choice(range(11111, 99999)))

# 2 Наличие Placeholder в поле Password
# def test_placeholder(self):
#     driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
#     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
#     placeholder = driver.find_element(by=By.XPATH,
#                                       value=".//input[@name='password' and @class='form-control form-control-sm input-dark']")
#     sleep(3)

# 3 Кликабельность кнопки Sign in - $x(".//button[@class='btn btn-primary btn-sm']")
# def test_sign_in(self):
#     '''Positive test with valid username and valid pass'''
#
#     driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
#     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
#     username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
#     username.clear()
#     username.send_keys("tatyanam")
#     sleep(3)
#     password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
#     password.clear()
#     password.send_keys("1234567890qwerty")
#     sleep(3)
#     button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
#     button.click()
#     logout = driver.find_element(by=By.XPATH, value=".//html/body/header/div/div/form/button")

# 4 Работоспособность рефки

# def test_link(self):
#     driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
#     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
#     link = driver.find_element(by=By.XPATH, value=".//a[@href='/'and @class='text-white']")
#     link.click()
#     sleep(3)
#
#     # 5 Наличие h1 на странице
#
# def test_h1(self):
#     driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
#     driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
#     h1 = driver.find_element(by=By.XPATH, value=".//H1")
#     # тут хочу сравнить текст найденного h1 с значением на стартовой странице, что бы было Тру, но не знаю как
#     sleep(3)


'''проверка таблицы'''
# import urllib.request
#
# import requests
# from html_table_parser import HTMLTableParser
#
#
# target = "http://htmlbook.ru/html/table"
#
#
# # get website content
# req = urllib.request.Request(url=target)
# f = urllib.request.urlopen(req)
# xhtml = f.read().decode('utf-8')
#
# # instantiate the parser and feed it
# p = HTMLTableParser()
# p.feed(xhtml)
# print(p.tables)
