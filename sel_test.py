from time import sleep

from attr import exceptions
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\daiyifan\\chromedriver_win32\\chromedriver.exe')
driver.get("https://y.qq.com/n/yqq/singer/0025NhlN2yWrP4.html")
##assert "Python" in driver.title  #assert用来测试表示式，其返回值为假，就会触发异常
print(driver.title)

# ele.clear()#网页上输入框的字无法自动消除
# ele.send_keys(" and some", Keys.ARROW_DOWN)
# ele.clear()#网页上输入框的字无法自动消除
# ele.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
for i in range(10):
    try:
        elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "js_song")))
        # actions = ActionChains(driver)
        # actions.move_to_element_with_offset(elements[i], 10,10)
        # actions.click()
        # actions.perform()
        # print(driver.title)
        # driver.back()
        print(driver.find_element_by_class_name("data__desc_txt").text)


    except exceptions.StaleElementReferenceException as e:
        print(e)



    # element = driver.find_element_by_xpath('//a[@class="js_song"]')
    # i=10
    # while i<=2:
    #     element.click()
    #     print(driver.title)
    #     sleep(5)
    #
    #     driver.back()
    #     sleep(5)
    #
    #     i=i+1
#e.click()
# all_options = element.find_elements_by_tag_name("option")
# for option in all_options:
#     print("Value is: %s" % option.get_attribute("value"))
#     option.click()
sleep(0)
driver.close()