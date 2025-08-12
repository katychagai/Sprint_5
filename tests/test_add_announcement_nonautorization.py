from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import Config
from src.locators import DoskaLocators


#Создание объявления неавторизованным пользователем

class TestDoskaAddAnnouncementWithoutAuth:
  
    def test_add_announcement_without_auth(self, driver):
        # 1. Открываем главную страницу
        driver.get(Config.URL)

        # 2. Нажать на кнопку Разместить объявление
        add_annt = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.ADD_ANNOUNCEMENT)
        )
        add_annt.click()

        # 3. Ожидаем модального окна - Чтобы разместить объявление, авторизуйтесь 
        auth_req_header = WebDriverWait(driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(DoskaLocators.AUTH_REQUIRED_HEADER)
        )
        
        # 4. Проверяем что модальное окно Чтобы разместить объявление, авторизуйтесь отображается
        assert auth_req_header.is_displayed()




