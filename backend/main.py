from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import random
from guara.transaction import AbstractTransaction, Application  # Corrected import


# Define Transactions
class NavigateToLoginPage(AbstractTransaction):
    def do(self, **kwargs):
        self._driver.get("http://192.168.1.46:8080")


class FillLoginForm(AbstractTransaction):
    def do(self, email, password, **kwargs):
        input_user = self._driver.find_element(By.XPATH, '//input[@id="email"]')
        input_user.click()
        self.send_keys_input(input_user, email)

        input_password = self._driver.find_element(By.XPATH, '//input[@id="password"]')
        input_password.click()
        self.send_keys_input(input_password, password)

        button_submit = self._driver.find_element(By.XPATH, '//button[@type="submit"]')
        button_submit.click()
        time.sleep(3)

    def send_keys_input(self, input, text):
        for letra in text:
            input.send_keys(letra)
            time.sleep(10 / random.randint(160, 300))


class AddPessoa(AbstractTransaction):
    def do(self, name, age, email, **kwargs):
        input_name = self._driver.find_element(By.XPATH, '//input[@id="name"]')
        input_name.click()
        input_name.send_keys(name)

        input_age = self._driver.find_element(By.XPATH, '//input[@id="age"]')
        input_age.click()
        input_age.send_keys(age)

        input_email = self._driver.find_element(By.XPATH, '//input[@id="email"]')
        input_email.click()
        input_email.send_keys(email)

        button_submit = self._driver.find_element(By.XPATH, '//button[@type="submit"]')
        button_submit.click()


class EditPessoa(AbstractTransaction):
    def do(self, id, name, age, email, **kwargs):
        button_edit = self._driver.find_element(
            By.XPATH, f'//button[@id="{id}" and contains(text(), "Editar")]'
        )
        button_edit.click()

        input_name = self._driver.find_element(By.XPATH, '//input[@id="name"]')
        input_name.click()
        input_name.clear()
        input_name.send_keys(name)

        input_age = self._driver.find_element(By.XPATH, '//input[@id="age"]')
        input_age.click()
        input_age.clear()
        input_age.send_keys(age)

        input_email = self._driver.find_element(By.XPATH, '//input[@id="email"]')
        input_email.click()
        input_email.clear()
        input_email.send_keys(email)

        button_submit = self._driver.find_element(By.XPATH, '//button[@type="submit"]')
        button_submit.click()


class DeletePessoa(AbstractTransaction):
    def do(self, id, **kwargs):
        button_delete = self._driver.find_element(
            By.XPATH, f'//button[@id="{id}" and contains(text(), "Excluir")]'
        )
        button_delete.click()


# Main Script
if __name__ == "__main__":
    # Initialize WebDriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    # Initialize Application
    app = Application(driver)

    # Perform actions using the Page Transactions pattern
    app.at(NavigateToLoginPage)
    app.at(FillLoginForm, email="teste@gmail.com.br", password="123")

    # Add pessoas
    app.at(AddPessoa, name="Joao", age=19, email="joao@hotmail.com")
    app.at(AddPessoa, name="Maria", age=20, email="maria@hotmail.com")
    app.at(AddPessoa, name="Marcos", age=21, email="marcos@hotmail.com")
    app.at(AddPessoa, name="Rose", age=21, email="rose@hotmail.com")

    # Edit pessoa
    app.at(EditPessoa, id=0, name="Joao Editado", age=19, email="joaoeditado@hotmail.com")

    # Delete pessoa
    app.at(DeletePessoa, id=2)

    # Close the driver
    driver.quit()
