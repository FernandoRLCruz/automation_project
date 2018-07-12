from selenium.webdriver.support.ui import WebDriverWait

'''classe base pra inicialização de todas page object classes'''
class BasePageElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_name(self.locator))
