class loginPage():
    def __init__(self, driver):
        self.driver = driver

        self.userName_textBox_xpath = "//input[@name='uname']"
        self.password_textBox_xpath= "//input[@name='pass']"
        self.login_button_xpath = "//input[@value='login']"
        self.signup_link_xpath = "//a[normalize-space()='Signup']"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.signup_link_xpath).click()
        self.driver.find_element_by_xpath(self.userName_textBox_xpath).clear()
        self.driver.find_element_by_xpath(self.userName_textBox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textBox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textBox_xpath).send_keys(password)

    def click_updatebutton(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()