from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import Config
from src.locators import DoskaLocators
from src.data import user_auth

#Регистрация существующего пользователя 

class TestDoskaRegistrationUserExt:
  
    def test_registration_user_ext(self, driver):
        # 1. Открываем главную страницу
        driver.get(Config.URL)
        
        # 2. Нажимаем кнопку авторизации
        auth_btn = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.AUTORIZATION_BUTTON)
        )
        auth_btn.click()
        
        # 3. Нажимаем кнопку "Нет аккаунта"
        no_acc_btn = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.BUTTON_NON_ACOUNT)
        )
        no_acc_btn.click()
        
        # 4. Заполняем форму регистрации
        email_ext, password_ext = user_auth()
        
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.EMAIL_FIELD)
        ).send_keys(email_ext)
        
        driver.find_element(*DoskaLocators.PASSWORD_FIELD).send_keys(password_ext)
        driver.find_element(*DoskaLocators.SUBMIT_PASSWORD).send_keys(password_ext)
        
        # 5. Нажимаем кнопку "Создать аккаунт"
        driver.find_element(*DoskaLocators.CREATE_ACC_BUTTON).click()

        # 6. Ожидаем подсвеченных полей красным, сообщение об ошибке
        error = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.ERROR_FIELD)
        )

        error_text = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.ERROR_TEXT)
        )
        
        # 7. Проверяем, что появилось сообщение об ошибке и поля подсвечены красным
        assert error.is_displayed()
        assert error_text.is_displayed()