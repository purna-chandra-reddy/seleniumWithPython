from selenium import webdriver
import time
import unittest
#import HTMLTestRunner

from pages.cartHelperFile import cartPage
from pages.guestBookHelperFile import guestBookPage
from pages.loginHelperFile import loginPage
from pages.userInfoHelperFile import updatePage


class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get("http://testphp.vulnweb.com/")
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.refresh()
        time.sleep(5)
        driver.get("http://testphp.vulnweb.com/login.php")
        login = loginPage(driver)
        time.sleep(4)
        login.enter_username("test")
        login.enter_password("test")
        login.click_updatebutton()

    def test_update_valid(self):
        driver = self.driver
        driver.refresh()
        time.sleep(5)
        driver.get("http://testphp.vulnweb.com/userinfo.php")
        time.sleep(5)
        update = updatePage(driver)
        time.sleep(4)
        update.update_userName("purna")
        update.creditCard_number("0000")
        update.phoneNumber("0000 0000")
        #update.address("bangalore")
        update.updateButton()

    def test_cartPage(self):
        driver = self.driver
        driver.get("http://testphp.vulnweb.com/cart.php")
        time.sleep(5)
        details = cartPage(driver)
        time.sleep(2)
        details.productsInfo()

    def test_guestBookPage(self):
        driver = self.driver
        driver.get("http://testphp.vulnweb.com/guestbook.php")
        time.sleep(5)
        guestBook = guestBookPage(driver)
        guestBook.messageBox("testing the page")
        guestBook.addMessageButton()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test execution completed successfully")

    @classmethod
    def implicitly_wait(cls, param):
        pass


if __name__ == '__main__':
    unittest.main()
#
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:\\pcr\\SeleniumExamples\\pomSelenium\\tests"))
