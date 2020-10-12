from selenium import webdriver

from proffile import Proffile
from web.academicwork import *
from web.altiusconsulting import *
from web.aplitrak import *
from web.danda import danda_action
from web.infotiv import infotiv_action
from web.ponty import *
from web.randstad import randstad_action
from web.recruto import *
from web.semconsweden import *
from web.softwareskills import *
from web.recruit import *


# def get_driver():
#     chrome_drive_path = r"C:\Users\User\AppData\Local\Programs\Python\Python38\Tools\chromedriver_win32\chromedriver.exe"
#     webdriver.Chrome(executable_path=chrome_drive_path).quit()
#     driver = webdriver.Chrome(executable_path=chrome_drive_path)
#     return webdriver.Chrome(executable_path=chrome_drive_path)


def open_link_in_chrome(url, id):
    profile = Proffile()
    # elif 'recruit.visma' in url:
    #     recruit_action(url, id,  profile)
    # elif 'aplitrak' in url:
    #     aplitrak_action(url, id,  profile)
    if 'academicwork' in url:
        academicwork_action(url, id, profile)
    elif 'randstad' in url:
        randstad_action(url, id, profile)
    elif 'pnty-apply.ponty-system.se' in url:
        ponty_action(url, id, profile)
    elif 'www.recruto.se' in url:
        recruto_action(url, id, profile)
    elif 'softwareskills' in url:
        softwareskills_action(url, id, profile)
    elif 'semconsweden' in url:
        semconsweden_actoin(url, id, profile)
    elif 'altiusconsulting' in url:
        altiusconsulting_action(url, id, profile)
    elif 'www.infotiv.se' in url:
        infotiv_action(url, id, profile)
    elif 'jobb.danda.se' in url:
        danda_action(url, id, profile)
    else:
        files.add_new_link_to_list(url, id, 'unlisted_links.csv')


if __name__ == '__main__':
    url = 'https://pnty-apply.ponty-system.se/friday?id=306&pnty_src=arbetsformedlingen'
    profile = Proffile()
    ponty_action(url, id, profile)
