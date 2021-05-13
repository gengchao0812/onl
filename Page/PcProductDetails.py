from Page.BasePage import BasePage
from Page.PcAuthentication import PcAuthentication

class PcProductDetails(BasePage):

    def goto_authentication(self):
        self._driver.find_element_by_xpath('//*[@class="detail_box"]//input[@class="btn btn-bank"]').click()
        self._driver.implicitly_wait(3)
        return PcAuthentication(self._driver)
