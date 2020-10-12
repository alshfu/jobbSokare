from selenium import webdriver
from time import sleep
import files

def infotiv_action(url, id, proffile):
    chrome_drive_path = r"C:\Users\User\AppData\Local\Programs\Python\Python38\Tools\chromedriver_win32\chromedriver.exe"
    webdriver.Chrome(executable_path=chrome_drive_path).quit()
    driver = webdriver.Chrome(executable_path=chrome_drive_path)
    driver.get(url)
    driver.implicitly_wait(5)
    sleep(5)
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    driver.find_elements_by_name('firstname')[0].send_keys(proffile.f_name())
    driver.find_elements_by_class_name('form-control')[1].send_keys(proffile.l_name())
    driver.find_elements_by_class_name('form-control')[2].send_keys(proffile.email())
    driver.find_elements_by_class_name('form-control')[3].send_keys(proffile.telefon())
    driver.find_elements_by_class_name('file')[0].send_keys(proffile.cv_file_location())
    driver.find_elements_by_class_name('file')[1].send_keys(proffile.cover_later_file_location())
    sleep(2)
    driver.find_element_by_id('open-pul').click()
    driver.find_elements_by_class_name('btn-primary')[0].click()
    sleep(5)
    files.add_new_link_to_list(url, id, 'link_list.csv')
    driver.quit()