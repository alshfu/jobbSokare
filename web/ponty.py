from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import files


def ponty_action(url, id, proffile):
    chrome_drive_path = r"C:\Users\User\AppData\Local\Programs\Python\Python38\Tools\chromedriver_win32\chromedriver.exe"
    webdriver.Chrome(executable_path=chrome_drive_path).quit()
    driver = webdriver.Chrome(executable_path=chrome_drive_path)
    driver.get(url)
    driver.implicitly_wait(5)
    sleep(2)
    driver.find_elements_by_tag_name('input')[0].send_keys(proffile.f_name())
    driver.find_element_by_id('lastname').send_keys(proffile.l_name())
    driver.find_element_by_id('email').send_keys(proffile.email())
    driver.find_element_by_id('phone').send_keys(proffile.telefon())
    driver.find_element_by_id('phone').send_keys(Keys.PAGE_DOWN)
    driver.find_element_by_id('phone').send_keys(Keys.PAGE_DOWN)
    driver.find_element_by_id('js-file_handler').send_keys(proffile.cv_file_location())
    driver.find_element_by_id('title').send_keys('freelance')
    driver.find_element_by_id('organization').send_keys('PODS')
    if len(driver.find_elements_by_class_name('fake-checkbox'))>1:
        checkboxs = driver.find_elements_by_class_name('fake-checkbox')
        for checkbox in checkboxs:
            checkbox.click()
            sleep(1)
    if driver.find_elements_by_class_name('slider'):
        print('Im hire!!!')
        driver.find_elements_by_class_name('fake-checkbox')[0].click()
        driver.find_elements_by_class_name('btn--primary')[0].click()
        sleep(15)
        files.add_new_link_to_list(url, id, 'link_list.csv')
        driver.quit()
    else:
        driver.find_elements_by_class_name('fake-checkbox')[0].click()
        driver.find_elements_by_class_name('btn--primary')[0].click()
        sleep(5)
        files.add_new_link_to_list(url, id, 'link_list.csv')
        driver.quit()
