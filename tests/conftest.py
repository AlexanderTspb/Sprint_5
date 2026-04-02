import pytest
from selenium import webdriver
import random

@pytest.fixture(scope="function")
def init_browser():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def generate_email_and_password():
    email = f'test{random.randint(1, 99999)}selenium-{random.randint(1, 99999)}@mail.ru'
    password = f'testpass-{random.randint(100, 999)}'
    credentials = {'email': email, 'password': password}
    print(f"Сгенерированы учётные данные: email={email}, password={password}")
    return credentials

@pytest.fixture(scope="function")
def generate_incorrect_email():
    email = f'test{random.randint(1, 99999)}selenium-{random.randint(1, 99999)}'
    print(f"Сгенерированы учётные данные: email={email}")
    return email

@pytest.fixture(scope="function")
def return_existing_acc():
    email = "testseleniumsprint5at@prak.com"
    password = "Adfhsagfa242+"
    credentials = {'email': email, 'password': password}
    return credentials
