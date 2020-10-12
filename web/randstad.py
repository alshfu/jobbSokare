from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import files


def randstad_action(url, id, proffile):
    chrome_drive_path = r"C:\Users\User\AppData\Local\Programs\Python\Python38\Tools\chromedriver_win32\chromedriver.exe"
    webdriver.Chrome(executable_path=chrome_drive_path).quit()
    driver = webdriver.Chrome(executable_path=chrome_drive_path)
    driver.get(url)
    driver.implicitly_wait(5)
    sleep(2)
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    driver.execute_script('document.getElementsByTagName("input")[7].style.display = "unset"')
    driver.execute_script('document.getElementsByTagName("input")[9].style.display = "unset"')
    sleep(3)
    driver.find_elements_by_class_name('form-control')[0].send_keys(proffile.f_name())
    driver.find_elements_by_class_name('form-control')[1].send_keys(proffile.l_name())
    driver.find_elements_by_class_name('form-control')[2].send_keys(proffile.email())
    driver.find_elements_by_class_name('form-control')[3].send_keys(proffile.telefon())
    driver.find_elements_by_class_name('form-control')[4].send_keys(proffile.street())
    driver.find_elements_by_class_name('form-control')[5].send_keys(proffile.zip_code())
    driver.find_elements_by_class_name('form-control')[6].send_keys(proffile.town())
    driver.find_elements_by_tag_name('input')[7].send_keys(proffile.cv_file_location())
    driver.find_elements_by_tag_name('input')[9].send_keys(proffile.cover_later_file_location())
    driver.find_elements_by_class_name('custom-checkbox')[1].click()
    sleep(2)
    driver.find_elements_by_class_name('btn-outline-primary')[2].click()
    sleep(5)
    files.add_new_link_to_list(url, id, 'link_list.csv')
    driver.quit()
