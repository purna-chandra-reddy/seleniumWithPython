class cartPage:
    def __init__(self, driver):
        self.driver = driver

        self.productRow_xpath = "//h3[normalize-space()='Total: $0']"
        self.productId_xpath = "//strong[normalize-space()='Product id']"
        self.title_xpath = "//strong[normalize-space()='Title']"
        self.artist_xpathh = "//strong[normalize-space()='Artist']"
        self.category_xpat = "//strong[normalize-space()='Category']"
        self.price_xpath = "//strong[normalize-space()='Price']"


    def productsInfo(self):
        element = self.driver.find_element_by_xpath(self.productRow_xpath)
        assert element.text == 'Total: $0'
    def productId(self):
        self.driver.find_element_by_xpath(self.productId_xpath)

    def title(self):
        self.driver.find_element_by_xpath(self.title_xpath)

    def artist(self):
        self.driver.find_element_by_xpath(self.artist_xpath)

    def category(self):
        self.driver.find_element_by_xpath(self.category_xpath)

    def price(self):
        self.driver.find_element_by_xpath(self.price_xpath).click()