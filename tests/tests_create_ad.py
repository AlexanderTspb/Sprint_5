from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from url import Urls
from data import ExistingAccountCredentials
from data import AdData

class TestCreate_ad:
    def test_create_ad_when_user_is_not_logged_in_shows_login_required(self, init_browser):
        
        init_browser.find_element(By.XPATH,Locators.place_an_ad_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.place_ad_login_form)))
        assert init_browser.current_url == Urls.login_page_url
    
    def test_create_ad_when_user_is_logged_in_succeeds(self, init_browser):
        
        init_browser.find_element(By.XPATH,Locators.login_and_registration_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.login_form)))
        email = ExistingAccountCredentials.credentials.get('email')
        password = ExistingAccountCredentials.credentials.get('password')
        init_browser.find_element(By.NAME,Locators.email_input_name_registration_form).send_keys(email)
        init_browser.find_element(By.NAME,Locators.password_input_name_registration_form).send_keys(password)
        init_browser.find_element(By.XPATH,Locators.login_button).click()
        WebDriverWait(init_browser, 10).until(expected_conditions.invisibility_of_element_located((By.XPATH,Locators.login_form)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, Locators.profile_avatar)))
        init_browser.find_element(By.XPATH,Locators.place_an_ad_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.new_ad_title)))
        init_browser.find_element(By.XPATH,Locators.ad_name_input).send_keys(AdData.ad_name)
        init_browser.find_element(By.XPATH,Locators.category_dropDown_button).click()
        init_browser.find_element(By.XPATH,Locators.category_dropDown_gardening_button).click()
        init_browser.find_element(By.XPATH,Locators.city_dropDown_button).click()
        init_browser.find_element(By.XPATH,Locators.city_dropDown_novosibirsk_button).click()
        init_browser.find_element(By.XPATH,Locators.bu_radio_input).click()
        init_browser.find_element(By.XPATH,Locators.ad_textarea_description).send_keys(AdData.ad_description)
        init_browser.find_element(By.XPATH,Locators.ad_price_input).send_keys(AdData.ad_price)
        init_browser.find_element(By.XPATH,Locators.ad_publish_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.invisibility_of_element_located((By.XPATH, Locators.new_ad_title)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.main_page_search_input)))
        init_browser.find_element(By.CSS_SELECTOR, Locators.profile_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.profile_title)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.ad_pagination)))
        element = init_browser.find_element(By.XPATH,Locators.ad_pagination)
        init_browser.execute_script("arguments[0].scrollIntoView();", element)
        product_cards = init_browser.find_elements(By.XPATH,Locators.cards_with_mandragora_title)
        assert len(product_cards) > 0
        city = init_browser.find_element(By.XPATH,Locators.cards_with_mandragora_city).text
        assert city == AdData.ad_city
