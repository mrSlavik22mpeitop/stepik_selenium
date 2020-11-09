from selenium import webdriver
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    print(y)



    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
