from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'twitch.txt')
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)


    input1 = browser.find_element_by_css_selector(".form-group :nth-child(2)")
    input1.send_keys("Vyacheslav")

    input2 = browser.find_element_by_css_selector(".form-group :nth-child(4)")
    input2.send_keys("Volgin")

    input3 = browser.find_element_by_css_selector(".form-group :nth-child(6)")
    input3.send_keys("mpei@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
