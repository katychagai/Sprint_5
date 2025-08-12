
from selenium.webdriver.common.by import By

class DoskaLocators:
    
    #кнопка регистрации
    AUTORIZATION_BUTTON = By.XPATH, "//button[@class='buttonSecondary inButtonText undefined inButtonText' and contains(text(),'Вход и регистрация')]"
    
    #кнопка войти, с существующим пользователем
    LOGIN_BUTTON = By.XPATH, "//button[contains(text(),'Войти')]"
    #"//button[@class='buttonPrimary inButtonText undefined inButtonText' and contains(text(),'Войти')]"
    
    #кнопка нет аккаунта
    BUTTON_NON_ACOUNT = By.XPATH, "//button[contains(text(),'Нет аккаунта')]"
    
    #поле емейл
    EMAIL_FIELD = By.XPATH, "//input[@name='email']"
    
    #поле пароль
    PASSWORD_FIELD = By.XPATH, "//input[@placeholder='Пароль']"
    
    #поле подтверждение пароля
    SUBMIT_PASSWORD = By.XPATH, "//input[@name='submitPassword']"
    
    #кнопка создать аккаунт
    CREATE_ACC_BUTTON = By.XPATH, "//button[contains(text(),'Создать аккаунт')]"
    
    #элемент аватар
    AVATAR_USER = By.XPATH, "//button[@class='circleSmall']//*[name()='svg']"
    
    #имя юзера
    NAME_USER = By.XPATH, "//h3[@class='profileText name']"

    #кнопка разместить объявление
    ADD_ANNOUNCEMENT = By.XPATH, "//button[@class='buttonPrimary inButtonText undefined inButtonText' and contains(text(),'Разместить объявление')]"

    ADD_LIST = By.XPATH, "//button[contains(text(),'Разместить объявление')]"

    #поле название в объявлении
    NAME_PRODUCT_FIELD = By.XPATH, '//input[@name="name" and contains(@class, "inputStandart")]'

    #поле описание в объявлении
    DESCRIPTION_PRODUCT_FIELD = By.XPATH, '//textarea[@name="description" and contains(@class, "inputStandart")]'
    
    #поле цена в объявлении
    PRICE_PRODUCT_FIELD = By.CSS_SELECTOR, 'input[name="price"]'

    #создать объявление
    CREATE_BUTTON = By.XPATH, "//button[@type='submit']"

    #кнопка Выход
    LOGOUT_BUTTON = By.XPATH, "//button[contains(text(),'Выйти')]"

    #поле поиска (для теста перехода на главную страницу)
    SEARCH_FIELD = By.CSS_SELECTOR, "input[name='name'],[accept='text']"

    #сообщение Ошибка под полем мейл
    ERROR_TEXT = By.XPATH, "//span[contains(text(),'Ошибка')]"

    #поля подсвеченные красным 
    ERROR_FIELD = By.XPATH, "//div[contains(@class, 'Error')]"

    #модальное окно Чтобы разместить объявление, авторизуйтесь
    AUTH_REQUIRED_HEADER = By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']"

    #страница Новое объявление 
    NEW_AD_HEADER = By.XPATH, "//h1[contains(@class, 'createListing_title__') and text()='Новое объявление']"

    #радибаттон состояние товара
    RADIO_BUTTON_EXC = By.CSS_SELECTOR, "div[class*='inputRegular__']"

    #Дропдаун категория
    DROPDOWN_CATEGORY_DOWN = By.XPATH, "//div[contains(@class, 'dropDownMenu_input') and .//input[@value='Авто']]//button[contains(@class, 'dropDownMenu_arrowDown')]"
    
    #Выбор категории
    CATEGORY_USE = By.XPATH, "//div[contains(@class, 'dropDownMenu_options')]//button[3]"

    #Дропдаун город
    DROPDOWN_CYTY = By.XPATH,"//div[contains(@class, 'dropDownMenu_input') and .//input[@value='Москва']]//button[contains(@class, 'dropDownMenu_arrowDown')]"

    #Выбор города
    CITY_USE = By.XPATH, "//div[contains(@class, 'dropDownMenu_options')]//button[2]"

    #Кнопка Опубликовать объявление
    SUBMIT_LIST = By.XPATH, '//button[text()="Опубликовать"]'
    
    #страница моего профиля
    MY_PROFILE = By.XPATH, "//h1[@class='h1 zeroMargin']"

    #добавленное объявление
    MY_LIST = By.CSS_SELECTOR, "div[class*='grid_threeColumns'] div:nth-child(1)"

    
    MY_ADS_HEADER = By.XPATH, "//h1[@class='h1' and text()='Мои объявления']"

    #Кнопка применить на главной странице
    SUBMIT_BUTTON = By.XPATH, "//button[@type='submit']"


