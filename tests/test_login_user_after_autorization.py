from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import Config
from src.locators import DoskaLocators
from src.data import user_auth

#Login пользователя

class TestDoskaLoginUser:
  
    def test_login_user(self, driver):
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

        # 5. Ждем появления имени юзера, аватарки и перехода на главную страницу
        avatar = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.AVATAR_USER)
        )
        username = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.NAME_USER)
        )
        
        search_field = driver.find_element(*DoskaLocators.SEARCH_FIELD)

        # 6. Проверяем, что перешли на главную страницу (появилась поле поиска), 
        # виден аватар и имя юзера отображается корректно
        assert search_field.is_displayed()
        assert avatar.is_displayed()
        assert "User." in username.text