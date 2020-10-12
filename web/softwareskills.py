from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import files

def softwareskills_action(url, id, proffile):
    chrome_drive_path = r"C:\Users\User\AppData\Local\Programs\Python\Python38\Tools\chromedriver_win32\chromedriver.exe"
    webdriver.Chrome(executable_path=chrome_drive_path).quit()
    driver = webdriver.Chrome(executable_path=chrome_drive_path)
    print('softwareskills: ' + url)
    driver.get(url)
    sleep(5)
    driver.find_elements_by_class_name('apply-button')[0].click()
    sleep(1)
    driver.find_elements_by_class_name('ng-pristine')[0].send_keys(Keys.SPACE)
    driver.find_elements_by_class_name('btn-secondary')[5].click()
    sleep(1)
    driver.find_elements_by_class_name('form-control')[0].send_keys(proffile.f_name() + ' ' + proffile.l_name())
    driver.find_elements_by_class_name('form-control')[1].send_keys(proffile.email())
    driver.find_elements_by_class_name('form-control')[2].send_keys(proffile.town())
    driver.find_elements_by_class_name('form-control')[3].send_keys('Sweden')
    driver.find_elements_by_class_name('btn-primary')[1].click()
    sleep(2)
    if len(driver.find_elements_by_class_name('form-control')) > 3:
        sleep(5)
        files.add_new_link_to_list(url, id, 'link_list.csv')
        driver.quit()
    else:
        driver.find_elements_by_class_name('form-control')[0].send_keys('3-4')
        driver.find_elements_by_class_name('form-control')[1].send_keys('Google.se')
        driver.find_elements_by_class_name('form-control')[2].send_keys('java,js,c++,python,php,swift,android,kotlin')
        driver.find_elements_by_class_name('btn-primary')[2].click()
        sleep(1)
        driver.find_elements_by_tag_name('input')[1].send_keys(proffile.cv_file_location())
        driver.find_elements_by_class_name('btn-primary')[2].click()
        sleep(1)
        driver.find_elements_by_class_name('btn-primary')[2].click()
        # redactor-editor
        sleep(1)
        driver.find_elements_by_class_name('redactor-editor')[0].send_keys(proffile.p_brev())
        driver.find_elements_by_class_name('btn-primary')[2].click()
        sleep(5)
        files.add_new_link_to_list(url, id, 'link_list.csv')
        driver.quit()
