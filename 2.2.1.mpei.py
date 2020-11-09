from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x = browser.find_element_by_id("num1")
    x_result = x.text
    x_mpei = int(x_result)

    y = browser.find_element_by_id("num2")
    y_result = y.text
    y_mpei = int(y_result)

    all_result = x_mpei + y_mpei
    print(all_result)
    all_result_result = str(all_result)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(all_result_result)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
