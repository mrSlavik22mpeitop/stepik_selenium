from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button1 = browser.find_element_by_id("solve")
    button1.click()

finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()
