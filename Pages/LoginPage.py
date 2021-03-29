class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        self.usernm_testbox_id = 'txtUsername'
        self.pwrd_textbox_id = 'txtPassword'
        self.login_button_id = 'btnLogin'

    def enter_usernm(self,username):
        self.driver.find_element_by_id(self.usernm_testbox_id).clear()
        self.driver.find_element_by_id(self.usernm_testbox_id).send_keys(username)

    def enter_pwrd(self,pwrd):
        self.driver.find_element_by_id(self.pwrd_textbox_id).clear()
        self.driver.find_element_by_id(self.pwrd_textbox_id).send_keys(pwrd)

    def click_logic(self):
        self.driver.find_element_by_id(self.login_button_id).click()


