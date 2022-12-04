from selenium.webdriver.common.by import By
from time import sleep

class Login:
    def __init__(self: object, email: str, password: str, driver: object):
        self._email: str = email
        self._password: str = password
        self._driver: object = driver

    @property
    def email(self: object) -> str:
        return self._email

    @property
    def password(self: object) -> str:
        return self._password

    @property
    def driver(self: object) -> object:
        return self._driver

    def login(self: object) -> None:
        link_login = continue_link = self.driver.find_element(By.LINK_TEXT, 'Entrar')
        link_login.click()
        sleep(2)

        username_field = self.driver.find_element(By.NAME, 'username')
        password_field = self.driver.find_element(By.NAME, 'password')

        confirm_button = self.driver.find_element(By.XPATH, '//*[@id="auth-modal"]/div/form/div[4]/button')
        sleep(2)

        username_field.send_keys(self.email)
        sleep(2)

        password_field.send_keys(self.password)
        text_field = self.driver.find_element(By.ID, 'g-recaptcha-response')
        print(text_field)

        #confirm_button.click()
