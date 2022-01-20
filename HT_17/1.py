# Завдання: за допомогою браузера (Selenium) відкрити форму за наступним посиланням:
# https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link
# заповнити і відправити її.
# Зберегти два скріншоти: заповненої форми і повідомлення про відправлення форми.
# В репозиторії скріншоти зберегти.
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


class DoScreenshot(object):
    def __init__(self):
        self.output_path = str(Path.cwd())
        preferences = {"download.default_directory": self.output_path,
                       "directory_upgrade": True,
                       "safebrowsing.enabled": True}
        options = ChromeOptions().add_experimental_option("prefs", preferences)
        self.wb = webdriver.Chrome('/home/kate/PycharmProjects/GeekHub2021/HT_17/chromedriver', options=options)

    def do(self):
        self.wb.get(
            'https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform')
        input_name = self.wb.find_element(By.CSS_SELECTOR, "input.quantumWizTextinputPaperinputInput")
        time.sleep(1)
        input_name.send_keys('Kateryna')
        self.wb.save_screenshot('screenshot1.png')

        button = self.wb.find_elements(By.CSS_SELECTOR,
                                       'span.appsMaterialWizButtonPaperbuttonContent.exportButtonContent')
        button[0].click()
        button_change = self.wb.find_elements(By.CSS_SELECTOR, 'div.freebirdFormviewerViewResponseLinksContainer a')
        href = button_change[0].get_attribute('href')
        return href

    def change(self):
        href = self.do()
        self.wb.get(href)
        change = self.wb.find_elements(By.CSS_SELECTOR, "input.quantumWizTextinputPaperinputInput.exportInput")
        change[1].clear()
        #time.sleep(10)
        change[1].send_keys('Kate45')
        self.wb.save_screenshot('screenshot2.png')
        button = self.wb.find_element(By.CSS_SELECTOR, 'span.appsMaterialWizButtonPaperbuttonLabel')
        button.click()
        self.wb.close()


DoScreenshot().change()