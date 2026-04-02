from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestLogin:
    def test_user_login_when_user_exists_succeeds(self, init_browser, return_existing_acc):

        init_browser.find_element(By.XPATH,Locators.login_and_registration_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.login_form)))
        email = return_existing_acc.get('email')
        password = return_existing_acc.get('password')
        init_browser.find_element(By.NAME,"email").send_keys(email)
        init_browser.find_element(By.NAME,"password").send_keys(password)
        init_browser.find_element(By.XPATH,Locators.login_button).click()
        WebDriverWait(init_browser, 10).until(expected_conditions.invisibility_of_element_located((By.XPATH,Locators.login_form)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "svgSmall")))
        user_name = init_browser.find_element(By.CSS_SELECTOR, ".profileText.name").text
        assert user_name == 'User.'
        assert init_browser.current_url == 'https://qa-desk.stand.praktikum-services.ru/'

    def test_user_logout_when_logged_in(self, init_browser, return_existing_acc):

        init_browser.find_element(By.XPATH,Locators.login_and_registration_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.login_form)))
        email = return_existing_acc.get('email')
        password = return_existing_acc.get('password')
        init_browser.find_element(By.NAME,"email").send_keys(email)
        init_browser.find_element(By.NAME,"password").send_keys(password)
        init_browser.find_element(By.XPATH,Locators.login_button).click()
        WebDriverWait(init_browser, 10).until(expected_conditions.invisibility_of_element_located((By.XPATH,Locators.login_form)))
        init_browser.find_element(By.XPATH,Locators.logout_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "svgSmall")))
        WebDriverWait(init_browser, 5).until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".profileText.name")))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.login_and_registration_button)))
        assert init_browser.current_url == 'https://qa-desk.stand.praktikum-services.ru/'
