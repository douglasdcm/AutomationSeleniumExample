from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import random

class SeleniumAutomator:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

    wait = WebDriverWait(driver, 10, 1)
    
    def main(self):
        print("Main2")
        self.driver.get("http://192.168.1.46:8080")

        input_user = self.driver.find_element(By.XPATH,'//input[@id="email"]')
        input_user.click()
        self.sendKeysInput(input_user, "teste@gmail.com.br")

        input_password = self.driver.find_element(By.XPATH,'//input[@id="password"]')
        input_password.click()
        self.sendKeysInput(input_password, "123")

        button_submit = self.driver.find_element(By.XPATH,'//button[@type="submit"]')
        button_submit.click()

        time.sleep(3)

        self.addPessoa("Joao",19,"joao@hotmail.com")
        self.addPessoa("Maria",20,"maria@hotmail.com")
        self.addPessoa("Marcos",21,"marcos@hotmail.com")
        self.addPessoa("Rose",21,"rose@hotmail.com")

        self.editPessoa(0,"Joao Editado",19,"joaoeditado@hotmail.com")
        self.deletePessoa(2)

    def sendKeysInput(self, input, text):
        for letra in text:
            input.send_keys(letra)
            time.sleep(10/random.randint(160,300))

    def addPessoa(self, name, age, email):
        input_name = self.driver.find_element(By.XPATH,'//input[@id="name"]')
        input_name.click()
        input_name.send_keys(name)

        input_age = self.driver.find_element(By.XPATH,'//input[@id="age"]')
        input_age.click()
        input_age.send_keys(age)

        input_email = self.driver.find_element(By.XPATH,'//input[@id="email"]')
        input_email.click()
        input_email.send_keys(email)

        button_submit = self.driver.find_element(By.XPATH,'//button[@type="submit"]')
        button_submit.click()
    
    def editPessoa(self, id ,name, age, email):
        button_edit = self.driver.find_element(By.XPATH,f'//button[@id="{id}" and contains(text(), "Editar")]')
        button_edit.click()

        input_name = self.driver.find_element(By.XPATH,'//input[@id="name"]')
        input_name.click()
        input_name.clear()
        input_name.send_keys(name)

        input_age = self.driver.find_element(By.XPATH,'//input[@id="age"]')
        input_age.click()
        input_age.clear()
        input_age.send_keys(age)

        input_email = self.driver.find_element(By.XPATH,'//input[@id="email"]')
        input_email.click()
        input_email.clear()
        input_email.send_keys(email)

        button_submit = self.driver.find_element(By.XPATH,'//button[@type="submit"]')
        button_submit.click()

    def deletePessoa(self, id):
        button_edit = self.driver.find_element(By.XPATH,f'//button[@id="{id}"  and contains(text(), "Excluir")]')
        button_edit.click()
    print("Hello World")

automator = SeleniumAutomator()
automator.main()