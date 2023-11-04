import subprocess
import time

import yaml
from testpage import OperationHelper
from api_func import auth,username
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

login = testdata['username']
password = testdata['password']


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401", "TEST1 FAIL"


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationHelper(browser)
    testpage.enter_login(login)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.auth() == f'Hello, {login}', "TEST2 FAIL"


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationHelper(browser)
    testpage.click_about_btn()
    title = 'About Page'
    time.sleep(2)
    assert title == testpage.check_title_about(), "TEST3 FAIL"


def test_step4(browser):
    logging.info("Test4 Starting")
    testpage = OperationHelper(browser)
    font_size = '32px'
    assert font_size == testpage.font_size_title(), "TEST4 FAIL"


def test_step5():
    #при неоходимости переиспользования можно вывести в отдельный файл команду для терминала
    logging.info("Test5 Starting")
    res = subprocess.run(f'nikto -h https://test-stand.gb.ru/ -ssl -Tuning 4', shell=True, stdout=subprocess.PIPE,
                         encoding='utf-8')
    if "0 error(s)" in res.stdout and res.returncode == 0:
        r = True
    assert r, "TEST5 FAIL"

def test_step6():
    logging.info("Test6 Starting")
    auth()
    assert username() == login, "TEST1 FAIL"


