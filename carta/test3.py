from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

gmailId = "btroncoso@cenabast.cl"
passWord = "Cena1920"

try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
        'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
        '&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    driver.implicitly_wait(15)

    loginBox = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    loginBox.send_keys(gmailId)

    nextButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]')))
    nextButton.click()

    passWordBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    passWordBox.send_keys(passWord)

    nextButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]')))
    nextButton.click()

    print('Inicio de sesión exitoso...!!')
except NoSuchElementException:
    print('No se encontró el elemento')
except TimeoutException:
    print('Tiempo de espera agotado')
except Exception as e:
    print(f'Error: {e}')
    print('Inicio de sesión fallido')
finally:
    service.stop()