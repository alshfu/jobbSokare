from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import files


def recruit_action(url, id, profile):
    chrome_drive_path = r"C:\Users\User\AppData\Local\Programs\Python\Python38\Tools\chromedriver_win32\chromedriver.exe"
    webdriver.Chrome(executable_path=chrome_drive_path).quit()
    driver = webdriver.Chrome(executable_path=chrome_drive_path)
    driver.get(url)
    driver.implicitly_wait(5)
    if driver.find_elements_by_class_name('VISMA_public_tile'):
        driver.find_element_by_id('ctl00_cphBody_btnApplyWithoutAccount').click()
        driver.implicitly_wait(5)
        public_apply_panel_application_fields = \
            driver.find_elements_by_class_name('public-apply-panel-application-fields')[0]
        public_apply_panel_application_fields.find_elements_by_tag_name('input')[1].send_keys(profile.f_name())
        public_apply_panel_application_fields.find_elements_by_tag_name('input')[2].send_keys(profile.l_name())
        public_apply_panel_application_fields.find_elements_by_tag_name('input')[3].send_keys(profile.email())
        public_apply_panel_application_fields.find_elements_by_tag_name('input')[4].send_keys(profile.email())
        public_apply_panel_application_fields.find_elements_by_tag_name('input')[5].send_keys(profile.telefon())
        public_apply_panel_application_fields.find_elements_by_tag_name('input')[6].send_keys(profile.b_date())
        public_apply_panel_application_fields.find_elements_by_tag_name('input')[7].send_keys(profile.email())
        public_apply_panel_application_fields.find_elements_by_tag_name('input')[8].click()
        public_apply_panel_application_fields.find_elements_by_tag_name('input')[13].send_keys(
            profile.cv_file_location())
        radioButtonWithFreeText = driver.find_elements_by_class_name('radioWithFreeText')
        radioButtonWithFreeText[0].send_keys(Keys.PAGE_DOWN)
        driver.implicitly_wait(5)
        for radio_button in radioButtonWithFreeText:
            radio_button.click()
        driver.find_elements_by_class_name('checkbox-inline')[0].find_elements_by_tag_name('input')[0].send_keys(
            Keys.SPACE)
        driver.find_elements_by_class_name('checkbox-inline')[0].find_elements_by_tag_name('input')[0].send_keys(
            Keys.PAGE_DOWN)
        sleep(10)
        driver.find_elements_by_class_name('icon24')[0].click()
        sleep(5)
        driver.quit()
    elif driver.find_elements_by_class_name('AR_wrapper'):
        driver.quit()
    else:
        driver.find_elements_by_class_name('radioWithFreeText')[0].click()
        driver.implicitly_wait(5)
        driver.quit()
    files.add_new_link_to_list(url, id, 'link_list.csv')
    driver.quit()
