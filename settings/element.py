from selenium.webdriver.support.ui import WebDriverWait

'''classe base pra inicialização de todas page object classes'''
class BasePageElement(object):
    def __set__(self, obj, value):
        '''Setar campo para um valor especifico'''
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

     def __get__(self, obj, value):
         '''Pegar texto de elemento na page'''
         driver = obj.driver
         WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_name(self.locator))
         element = driver.find_element_by_name(self.locator)
         return element.get_attribute(value)

