class HomePage():
    def __init__(self,driver):
        self.driver = driver

        self.wlcm_link_id = 'welcome'
        self.logout_btn_link_txt = 'Logout'

    def click_welcome(self):
        self.driver.find_element_by_id(self.wlcm_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_btn_link_txt).click()
