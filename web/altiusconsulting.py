from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import files

def altiusconsulting_action(url, id, proffile):
    chrome_drive_path = r"C:\Users\User\AppData\Local\Programs\Python\Python38\Tools\chromedriver_win32\chromedriver.exe"
    webdriver.Chrome(executable_path=chrome_drive_path).quit()
    driver = webdriver.Chrome(executable_path=chrome_drive_path)
    driver.get(url)
    driver.implicitly_wait(5)
    sleep(1)
    driver.find_elements_by_class_name('btn-apply')[0].click()
    sleep(5)
    driver.find_elements_by_class_name('form-control')[0].send_keys(proffile.f_name())
    driver.find_elements_by_class_name('form-control')[1].send_keys(proffile.l_name())
    driver.find_elements_by_class_name('form-control')[1].send_keys(Keys.PAGE_DOWN)
    driver.find_elements_by_class_name('form-control')[2].send_keys(proffile.email())
    driver.find_elements_by_class_name('form-control')[3].send_keys(proffile.telefon())
    driver.find_elements_by_class_name('checkbox')[5].click()
    driver.find_elements_by_class_name('form-control')[4].send_keys(proffile.cv_file_location())
    driver.find_elements_by_class_name('form-control')[15].send_keys(proffile.p_brev())
    driver.find_elements_by_class_name('btn-apply')[2].click()
    sleep(5)
    files.add_new_link_to_list(url, id, 'link_list.csv')
    driver.quit()