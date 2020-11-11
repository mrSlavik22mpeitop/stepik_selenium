from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

def registration(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block :nth-child(1) > input")
        input1.send_keys("Vyacheslav")
        input2 = browser.find_element_by_css_selector(".first_block :nth-child(2) > input")
        input2.send_keys("Volgin")
        input3 = browser.find_element_by_css_selector(".first_block :nth-child(3) > input")
        input3.send_keys("mrslavik22@mpei.top")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # находим элемент, содержащий текст
        # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        browser.quit()
        return welcome_text

class TestWebMPEITYPONETOP(unittest.TestCase):
    def test_test_web_typo_1(self):
        self.assertEqual(registration("http://suninjuly.github.io/registration1.html"),"Congratulations! You have successfully registered!","moscow1")

    def test_test_web_typo_2(self):
        self.assertEqual(registration("http://suninjuly.github.io/registration2.html"),"Congratulations! You have successfully registered!","moscow2")


if __name__ == "__main__":
    unittest.main()