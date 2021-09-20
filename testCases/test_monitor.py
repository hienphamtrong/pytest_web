import openpyxl
from utilities.customLogger import LogGen
import time


class Test_002_Monitor:
    baseURL = "http://127.0.0.1/monitor"
#    username = "admin@yourstore.com"
#    password = "admin"
    logger = LogGen.loggen()
    play_button_xpath = "(//mat-icon[contains(text(),'play')])"
    stop_button_xpath = "(//mat-icon[contains(text(),'stop')])"
    save_image_button_xpath = "(//mat-icon[contains(text(),'save')])"
    options_button_xpath = "//mat-icon[contains(text(),'more_vert')]"
    #monitor_item_xpath = "(//button[@role='menuitem'])[2]"
    #monitor_item_xpath = '/html/body/div/div[2]/div/div/div[2]/button'
    menu_button_xpath = "//mat-icon[contains(text(),'menu')]"

    high_radio_xpath = "//mat-radio-button[@id='mat-radio-2']"
    medium_radio_xpath = "//mat-radio-button[@id='mat-radio-3']"
    low_radio_xpath = "//mat-radio-button[@id='mat-radio-4']"
    all_radio_xpath = "//mat-radio-button[@id='mat-radio-6']"
    pos_radio_xpath = "//mat-radio-button[@id='mat-radio-7']"
    nega_radio_xpath = "//mat-radio-button[@id='mat-radio-8']"


    def test_monitor_button(self, setup):
        self.logger.info("**********Test_002_Monitor***************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        #self.driver.find_element_by_xpath(self.menu_button_xpath).click()
        #self.driver.find_element_by_xpath(self.monitor_item_xpath).click()

        self.driver.find_element_by_xpath(self.stop_button_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.play_button_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.save_image_button_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.options_button_xpath).click()
        time.sleep(5)
        self.driver.quit()

    def test_radio_button(self,setup):

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.find_element_by_xpath(self.options_button_xpath).click()
        time.sleep(10)
        self.driver.find_element_by_xpath(self.medium_radio_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.low_radio_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.high_radio_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.all_radio_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.pos_radio_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.nega_radio_xpath).click()


        self.driver.quit()









