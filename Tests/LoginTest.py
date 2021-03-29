from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import allure
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from UnitTestTutorial.PomProjectUnitTest.Pages.HomePage import HomePage
from UnitTestTutorial.PomProjectUnitTest.Pages.LoginPage import LoginPage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Driver/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

        # login on the website
        login = LoginPage(self.driver)
        login.enter_usernm('Admin')
        login.enter_pwrd('admin123')
        login.click_logic()

        # logout from the website
        homepage = HomePage(self.driver)
        homepage.click_welcome()
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')

if __name__ =='__main__':
    unittest.main()