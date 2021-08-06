class guestBookPage:
    def __init__(self, driver):
        self.driver = driver

        self.userName_list_xpath = "//td[@valign='middle']"
        self.messagedTime_xpath = "//td[normalize-space()='08.05.2021, 9:40 am']"
        self.messageIcon_xpath = "//img[@src='/images/remark.gif']"
        self.message_info_xpath = "//tbody/tr[3]/td[1]"
        self.messageBox_text_xpath = "//textarea[@name='text']"
        self.addMessage_button_css = "//input[@name='submit']"

    def userName(self):
        name = self.driver.find_element_by_xpath(self.userName_list_xpath)

    def messageTime(self):
        return self.driver.find_element_by_xpath(self.messagedTime_xpath)

    def messageIcon(self):
        return self.driver.find_element_by_xpath(self.messageIcon_xpath)

    def messageInfo(self):
        return self.driver.find_element_by_xpath(self.message_info_xpath)

    def messageBox(self, message):
        self.driver.find_element_by_xpath(self.messageBox_text_xpath).clear()
        self.driver.find_element_by_xpath(self.messageBox_text_xpath).send_keys(message)

    def addMessageButton(self):
        return self.driver.find_element_by_xpath(self.addMessage_button_css).click()
