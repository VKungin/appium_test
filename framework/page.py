class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element):
        return self.driver.find_element(element)

    def click_element(self, element):
        element.click()
