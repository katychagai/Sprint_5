from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import Config
from src.locators import DoskaLocators
from src.helpers import autorization

#Тест регистрации нового пользователя

class TestDoskaRegistrationNewUser:
  
    def test_registration_new_user(self, driver):
        # 1. Открываем главную страницу
        driver.get(Config.URL)
        
        # 2. Нажимаем кнопку авторизации
        auth_button = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.AUTORIZATION_BUTTON)
        )
        auth_button.click()
        
        # 3. Нажимаем кнопку "Нет аккаунта"
        no_acc_btn = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.BUTTON_NON_ACOUNT)
        )
        no_acc_btn.click()
        
        # 4. Заполняем форму регистрации
        email, password = autorization()
        
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.EMAIL_FIELD)
        ).send_keys(email)
        
        driver.find_element(*DoskaLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*DoskaLocators.SUBMIT_PASSWORD).send_keys(password)
        
        # 5. Нажимаем кнопку "Создать аккаунт"
        driver.find_element(*DoskaLocators.CREATE_ACC_BUTTON).click()
        
        # 6. Ждем появления имени юзера, аватарки и перехода на главную страницу
        avatar = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.AVATAR_USER)
        )
        username = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.NAME_USER)
        )
        
        search_field = driver.find_element(*DoskaLocators.SEARCH_FIELD)

        # 7. Проверяем, что перешли на главную страницу (появилась поле поиска), 
        # виден аватар и имя юзера отображается корректно
        assert search_field.is_displayed()
        assert avatar.is_displayed()
        assert "User." in username.text


    


        

   



        


