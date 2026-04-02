from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestCreate_ad:
    def test_create_ad_when_user_is_not_logged_in_shows_login_required(self, init_browser):
        
        init_browser.find_element(By.XPATH,Locators.place_an_ad_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.place_ad_login_form)))
        assert init_browser.current_url == 'https://qa-desk.stand.praktikum-services.ru/login'
    
    def test_create_ad_when_user_is_logged_in_succeeds(self, init_browser, return_existing_acc):
        
        init_browser.find_element(By.XPATH,Locators.login_and_registration_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.login_form)))
        email = return_existing_acc.get('email')
        password = return_existing_acc.get('password')
        init_browser.find_element(By.NAME,"email").send_keys(email)
        init_browser.find_element(By.NAME,"password").send_keys(password)
        init_browser.find_element(By.XPATH,Locators.login_button).click()
        WebDriverWait(init_browser, 10).until(expected_conditions.invisibility_of_element_located((By.XPATH,Locators.login_form)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "svgSmall")))
        init_browser.find_element(By.XPATH,Locators.place_an_ad_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.new_ad_title)))
        init_browser.find_element(By.XPATH,Locators.ad_name_input).send_keys('Мандрагора')
        init_browser.find_element(By.XPATH,Locators.category_dropDown_button).click()
        init_browser.find_element(By.XPATH,Locators.category_dropDown_gardening_button).click()
        init_browser.find_element(By.XPATH,Locators.city_dropDown_button).click()
        init_browser.find_element(By.XPATH,Locators.city_dropDown_novosibirsk_button).click()
        init_browser.find_element(By.XPATH,Locators.bu_radio_input).click()
        init_browser.find_element(By.XPATH,Locators.ad_textarea_description).send_keys("Мандрагора (Mandragora magica) — в наличии! \n Свежий урожай волшебных мандрагор. Подходят для: \n зельеварения (Восстанавливающее зелье и др.) \n магической ботаники; \n коллекционирования")
        init_browser.find_element(By.XPATH,Locators.ad_price_input).send_keys(50)
        init_browser.find_element(By.XPATH,Locators.ad_publish_button).click()
        WebDriverWait(init_browser, 5).until(expected_conditions.invisibility_of_element_located((By.XPATH, Locators.new_ad_title)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.main_page_search_input)))
        init_browser.find_element(By.CLASS_NAME, "circleSmall").click()
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.profile_title)))
        WebDriverWait(init_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH,Locators.ad_pagination)))
        element = init_browser.find_element(By.XPATH,Locators.ad_pagination)
        init_browser.execute_script("arguments[0].scrollIntoView();", element)
        product_cards = init_browser.find_elements(By.XPATH,Locators.cards_with_mandragora_title)
        assert len(product_cards) > 0
        city = init_browser.find_element(By.XPATH,Locators.cards_with_mandragora_city).text
        assert city == 'Новосибирск'
