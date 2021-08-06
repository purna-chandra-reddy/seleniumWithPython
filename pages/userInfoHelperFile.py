import time


class updatePage:
    def __init__(self, driver):
        self.driver = driver

        self.userName_textBox_xpath="//input[@name='urname']"
        self.creditCard_textBox_xpath = "//input[@name='ucc']"
        self.emailId_textBox_xpath="//input[@name='uemail']"
        self.phoneNumber_textBox_xpath = "//input[@name='uphone']"
        self.address_textBox_xpath = "//textarea[@name='uaddress']"
        self.updateButton_xpath = "//input[@name='update']"

    def update_userName(self, newUserName):
        self.driver.find_element_by_xpath(self.userName_textBox_xpath).clear()
        self.driver.find_element_by_xpath(self.userName_textBox_xpath).send_keys(newUserName)

    def creditCard_number(self, number):
        self.driver.find_element_by_xpath(self.creditCard_textBox_xpath).clear()
        self.driver.find_element_by_xpath(self.creditCard_textBox_xpath).send_keys(number)

    def phoneNumber(self, number):
        self.driver.find_element_by_xpath(self.phoneNumber_textBox_xpath).clear()
        self.driver.find_element_by_xpath(self.phoneNumber_textBox_xpath).send_keys(number)

    def address(self, address):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.address_textBox_xpath).clear()
        time.sleep(3)
        self.driver.find_element_by_xpathe(self.address_textBox_xpath).send_keys(address)

    def updateButton(self):
        self.driver.find_element_by_xpath(self.updateButton_xpath).click()
