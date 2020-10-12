from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import files


def academicwork_action(url, id, proffile):
    chrome_drive_path = r"C:\Users\User\AppData\Local\Programs\Python\Python38\Tools\chromedriver_win32\chromedriver.exe"
    webdriver.Chrome(executable_path=chrome_drive_path).quit()
    driver = webdriver.Chrome(executable_path=chrome_drive_path)
    driver.get(url)
    driver.find_elements_by_class_name('aw-block-button')[1].click()
    driver.find_element_by_id('username').send_keys(proffile.email())
    driver.find_element_by_id('password').send_keys(proffile.password())
    driver.find_element_by_id('login-btn').click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'web-cv-container')))
    sleep(5)
    aw_default_button_for_cv = driver.find_elements_by_class_name('aw-default-button')[3]
    aw_default_button_for_cv.find_element_by_name('UploadCv').send_keys(proffile.cv_file_location())
    driver.find_elements_by_class_name('aw-button-application')[3].click()
    sleep(5)
    driver.find_elements_by_class_name('aw-button-application')[0].click()
    sleep(5)
    driver.find_elements_by_class_name('aw-button-application')[0].click()
    sleep(5)
    files.add_new_link_to_list(url, id, 'link_list.csv')
    driver.quit()
