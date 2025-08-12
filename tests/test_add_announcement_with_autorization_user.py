from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import Config
from src.locators import DoskaLocators
from src.data import user_auth


class TestDoskaAddAnnouncementWithAuth:
  
    def test_add_announcement_with_auth(self, driver):

        # 1. Открываем главную страницу
        driver.get(Config.URL)

        # 2. Нажимаем кнопку авторизации
        auth_btn = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.AUTORIZATION_BUTTON)
        )
        auth_btn.click()

        # 3. Заполняем поля формы авторизации
        email_ext, password_ext = user_auth()
        
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.EMAIL_FIELD)
        ).send_keys(email_ext)
        
        driver.find_element(*DoskaLocators.PASSWORD_FIELD).send_keys(password_ext)

        # 4. Нажимаем кнопку Войти 
        login_button = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.LOGIN_BUTTON)
        )
        login_button.click()

        # 5. Ждем перехода на главную появление аватара юзера 
        WebDriverWait(driver, Config.TIMEOUT).until(
                EC.visibility_of_element_located(DoskaLocators.AVATAR_USER)
            )

        # 5. Нажимаем кнопку создать объявление
        add_button = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.element_to_be_clickable(DoskaLocators.ADD_LIST)
        )      
        add_button.click()
        
        # 6. Ждем загрузки страницы Новое объявление
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.NEW_AD_HEADER)
        )

        # 7. Заполняем поле наименование
        name_product_field = driver.find_element(*DoskaLocators.NAME_PRODUCT_FIELD)
        name_product_field.send_keys('Продам козу')

        # 8.Заполняем поле описание
        description_product_field = driver.find_element(*DoskaLocators.DESCRIPTION_PRODUCT_FIELD)
        description_product_field.send_keys('Много не кушает. Дает молоко')

        # 9. Заполняем поле цена
        price_product_field = driver.find_element(*DoskaLocators.PRICE_PRODUCT_FIELD)
        price_product_field.send_keys('1000')

        # 10. Выбираем категорию
        category = driver.find_element(*DoskaLocators.DROPDOWN_CATEGORY_DOWN)
        category.click()

        category_use = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.CATEGORY_USE)
        )
        category_use.click()

        # 11. Выбираем город
        city = driver.find_element(*DoskaLocators.DROPDOWN_CYTY)
        city.click()

        city_use = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.CITY_USE)
        )
        city_use.click()

        # 12. Выбираем состояние 
        condition_prod = driver.find_element(*DoskaLocators.RADIO_BUTTON_EXC)
        condition_prod.click()

        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.RADIO_BUTTON_EXC)
        )

        # 13. Нажимаем кнопку создать
        create_list = driver.find_element(*DoskaLocators.SUBMIT_LIST)
        create_list.click()

        # 14. Проверяем переход на главную страницу
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.element_to_be_clickable(DoskaLocators.SUBMIT_BUTTON)
        )

        # 15. Нажимаем на аватар, чтобы перейти в мой профиль

        avatar_user = driver.find_element(*DoskaLocators.AVATAR_USER)
        driver.execute_script("arguments[0].scrollIntoView();", avatar_user)
        avatar_user.click()

        # 16. Ожидаем появления страницы профиля и секции Мои объявления 
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.MY_LIST)
        )
        
        my_list = driver.find_element(*DoskaLocators.MY_LIST)
        
        #проверяем, что в моих объявлениях есть новое объявление 
        assert my_list.is_displayed()