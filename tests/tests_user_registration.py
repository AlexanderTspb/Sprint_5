from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestRegistration:
    def test_user_registration_when_user_doesnt_exist_succeeds(self, init_browser, generate_email_and_password):

        init_browser.find_element(By.XPATH, Locators.login_and_registration_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.login_form)))
        init_browser.find_element(By.XPATH,Locators.no_account_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.registration_form)))
        email = generate_email_and_password.get('email')
        password = generate_email_and_password.get('password')
        init_browser.find_element(By.NAME,"email").send_keys(email)
        init_browser.find_element(By.NAME,"password").send_keys(password)
        init_browser.find_element(By.NAME,"submitPassword").send_keys(password)
        init_browser.find_element(By.XPATH,Locators.create_account_button).click()
        WebDriverWait(init_browser, 10).until(expected_conditions.invisibility_of_element_located((By.XPATH,Locators.registration_form)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "svgSmall")))
        user_name = init_browser.find_element(By.CSS_SELECTOR, ".profileText.name").text
        assert user_name == 'User.'
        assert init_browser.current_url == 'https://qa-desk.stand.praktikum-services.ru/'

    def test_user_registration_when_email_is_incorrect_shows_error(self, init_browser, generate_incorrect_email):

        init_browser.find_element(By.XPATH,Locators.login_and_registration_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.login_form)))
        init_browser.find_element(By.XPATH,Locators.no_account_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.registration_form)))
        email = generate_incorrect_email
        init_browser.find_element(By.NAME,"email").send_keys(email)
        init_browser.find_element(By.XPATH,Locators.create_account_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.email_input_error)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.password_input_error)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.submit_password_input_error)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.email_input_error_text)))
        assert init_browser.find_element(By.XPATH,Locators.email_input_error_span).text == 'Ошибка'
    
    def test_user_registration_when_user_already_exists_shows_error(self, init_browser, return_existing_acc):

        init_browser.find_element(By.XPATH,Locators.login_and_registration_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.login_form)))
        init_browser.find_element(By.XPATH,Locators.no_account_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.registration_form)))
        email = return_existing_acc.get('email')
        password = return_existing_acc.get('password')
        init_browser.find_element(By.NAME,"email").send_keys(email)
        init_browser.find_element(By.NAME,"password").send_keys(password)
        init_browser.find_element(By.NAME,"submitPassword").send_keys(password)
        init_browser.find_element(By.XPATH,Locators.create_account_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.email_input_error)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.password_input_error)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.submit_password_input_error)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.email_input_error_text)))
        assert init_browser.find_element(By.XPATH,Locators.email_input_error_span).text == 'Ошибка'
