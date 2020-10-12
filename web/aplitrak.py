from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import files


def aplitrak_action(url, id, proffile):
    chrome_drive_path = r"C:\Users\User\AppData\Local\Programs\Python\Python38\Tools\chromedriver_win32\chromedriver.exe"
    webdriver.Chrome(executable_path=chrome_drive_path).quit()
    driver = webdriver.Chrome(executable_path=chrome_drive_path)
    driver.get(url)
    driver.implicitly_wait(15)
    driver.find_elements_by_class_name('gwt-TextBox')[0].send_keys(proffile.email())
    driver.find_elements_by_class_name('gwt-PasswordTextBox')[0].send_keys(proffile.password_secondary())
    driver.find_elements_by_class_name('gwt-PasswordTextBox')[0].send_keys(Keys.ENTER)
    sleep(5)
    skeep = 'Вы уже подавали заявление о приеме на работу на эту вакансию.'
    if skeep in driver.find_elements_by_class_name('WFOO')[0].text:
        driver.quit()
    else:
        driver.find_elements_by_class_name('WMEN')[3].click()
        sleep(5)
        driver.find_elements_by_class_name('gwt-TextBox')[0].send_keys(proffile.f_name())
        driver.find_elements_by_class_name('gwt-TextBox')[1].send_keys(proffile.l_name())
        driver.find_elements_by_class_name('gwt-TextBox')[4].send_keys(
            proffile.street() + ' ' + proffile.street_number())
        driver.find_elements_by_class_name('gwt-TextBox')[4].send_keys(Keys.PAGE_DOWN)
        driver.find_elements_by_class_name('gwt-TextBox')[5].send_keys(proffile.zip_code())
        driver.find_elements_by_class_name('gwt-TextBox')[6].send_keys(proffile.town())
        driver.find_elements_by_class_name('gwt-TextBox')[8].send_keys(proffile.telefon())
        driver.find_elements_by_class_name('gwt-TextBox')[8].send_keys(Keys.PAGE_DOWN)
        driver.find_elements_by_class_name('WAG0')[1].send_keys(Keys.ENTER)
        driver.find_elements_by_class_name('WAG0')[1].send_keys(Keys.DOWN)
        driver.find_elements_by_class_name('WAG0')[1].send_keys(Keys.ENTER)
        driver.find_elements_by_class_name('WMEN')[7].click()
        sleep(5)
        driver.find_elements_by_class_name('WMEN')[10].click()
        sleep(5)
        driver.find_elements_by_class_name('WAG0')[0].send_keys(Keys.ENTER)
        driver.find_elements_by_class_name('WAG0')[0].send_keys(Keys.DOWN)
        driver.find_elements_by_class_name('WAG0')[0].send_keys(Keys.DOWN)
        driver.find_elements_by_class_name('WAG0')[0].send_keys(Keys.ENTER)
        driver.find_elements_by_class_name('WAG0')[1].send_keys(Keys.ENTER)
        driver.find_elements_by_class_name('WAG0')[1].send_keys(Keys.DOWN)
        driver.find_elements_by_class_name('WAG0')[1].send_keys(Keys.ENTER)
        driver.find_elements_by_class_name('WAG0')[2].send_keys(Keys.ENTER)
        driver.find_elements_by_class_name('WAG0')[2].send_keys(Keys.DOWN)
        driver.find_elements_by_class_name('WAG0')[2].send_keys(Keys.DOWN)
        driver.find_elements_by_class_name('WAG0')[2].send_keys(Keys.ENTER)
        driver.find_elements_by_class_name('WAG0')[3].send_keys(Keys.ENTER)
        driver.find_elements_by_class_name('WAG0')[3].send_keys(Keys.DOWN)
        driver.find_elements_by_class_name('WAG0')[3].send_keys(Keys.DOWN)
        driver.find_elements_by_class_name('WAG0')[3].send_keys(Keys.ENTER)
        driver.find_elements_by_class_name('WMEN')[2].click()
        sleep(5)
        files.add_new_link_to_list(url, id, 'link_list.csv')
        driver.quit()
