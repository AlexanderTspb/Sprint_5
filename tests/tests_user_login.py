from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from url import Urls
from data import ExistingAccountCredentials

class TestLogin:
    def test_user_login_when_user_exists_succeeds(self, init_browser):

        init_browser.find_element(By.XPATH,Locators.login_and_registration_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.login_form)))
        email = ExistingAccountCredentials.credentials.get('email')
        password = ExistingAccountCredentials.credentials.get('password')
        init_browser.find_element(By.NAME,Locators.email_input_name_registration_form).send_keys(email)
        init_browser.find_element(By.NAME,Locators.password_input_name_registration_form).send_keys(password)
        init_browser.find_element(By.XPATH,Locators.login_button).click()
        WebDriverWait(init_browser, 10).until(expected_conditions.invisibility_of_element_located((By.XPATH,Locators.login_form)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, Locators.profile_avatar)))
        user_name = init_browser.find_element(By.CSS_SELECTOR, Locators.profile_user_name).text
        assert user_name == ExistingAccountCredentials.user_name
        assert init_browser.current_url == Urls.main_page_url

    def test_user_logout_when_logged_in(self, init_browser):

        init_browser.find_element(By.XPATH,Locators.login_and_registration_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.login_form)))
        email = ExistingAccountCredentials.credentials.get('email')
        password = ExistingAccountCredentials.credentials.get('password')
        init_browser.find_element(By.NAME,Locators.email_input_name_registration_form).send_keys(email)
        init_browser.find_element(By.NAME,Locators.password_input_name_registration_form).send_keys(password)
        init_browser.find_element(By.XPATH,Locators.login_button).click()
        WebDriverWait(init_browser, 10).until(expected_conditions.invisibility_of_element_located((By.XPATH,Locators.login_form)))
        init_browser.find_element(By.XPATH,Locators.logout_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, Locators.profile_avatar)))
        WebDriverWait(init_browser, 5).until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, Locators.profile_user_name)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.login_and_registration_button)))
        assert init_browser.current_url == Urls.main_page_url
