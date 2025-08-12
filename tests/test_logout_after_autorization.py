
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import Config
from src.locators import DoskaLocators
from src.data import user_auth

#Logout пользователя 

class TestDoskaLogoutUser:
  
    def test_logout_user(self, driver):
        # 1. Открываем главную страницу
        driver.get(Config.URL)
        
        # 2. Нажимаем кнопку авторизации
        auth_btn = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.AUTORIZATION_BUTTON)
        )
        auth_btn.click()

        # 3. Заполняем форму регистрации
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

        # 5. Ожидаем появления кнопки Выйти и нажимаем на кнопку Выйти 
        logout_button = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

         # 6. Ожидаем появления кнопки авторизации
        auth_btn = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.AUTORIZATION_BUTTON)
        )

        assert auth_btn.is_displayed()

        # 7. Проверка, что элементы Аватар и Юзер нейм отсутствуют
        assert len(driver.find_elements(*DoskaLocators.AVATAR_USER)) == 0
        assert len(driver.find_elements(*DoskaLocators.NAME_USER)) == 0
