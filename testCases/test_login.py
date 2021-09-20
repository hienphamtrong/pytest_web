import openpyxl
from utilities.customLogger import LogGen
from selenium import webdriver
import time


class Test_001_Login:
    baseURL = "http://127.0.0.1"

    logger = LogGen.loggen()
    cell_xpath = "(//*[contains(@class,'column')])"
    row_xpath = "(//*[@role='row'])"
    menuitem_xpath = "(//button[@role='menuitem'])"
    menubutton_xpath = "//mat-icon[contains(text(),'menu')]"

    wb = openpyxl.load_workbook('TestData/sample.xlsx')

    def test_homePageTitle(self, setup):
        self.logger.info("**********Test_001_Login***************")
        self.logger.info("**********Verifying Home Page***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.quit()
        if act_title == "Matrix - Web Page":
            assert True
            self.logger.info("**********Home page title test is passed***************")
        else:
            self.logger.error("**********Home page title test is Failed***************")
            assert False

    def test_data(self, setup):
        flag = True
        self.driver = setup
        self.driver.get(self.baseURL)
        self.num_cells = len(self.driver.find_elements_by_xpath(self.cell_xpath))
        self.num_rows = len(self.driver.find_elements_by_xpath(self.row_xpath))
        self.logger.info(str(self.num_cells) + " cells")
        num_col = int(self.num_cells / self.num_rows)
        for row in range(1, self.num_rows+1):
            for col in range(1, num_col+1):
                t_cell = row*num_col - (num_col-col)
                char = chr(64+col)
                read_data = self.wb['Sheet2'][char + str(row)].value
                text = self.driver.find_element_by_xpath(self.cell_xpath + '[' + str(t_cell) + ']').text
                if(str(read_data)!=text):
                    flag = False
                    self.logger.error("Expected: " + str(read_data) + " but Observed:" + text)
        self.driver.quit()
        if (flag == False):
            assert False

    def test_menu_button(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.find_element_by_xpath(self.menubutton_xpath).click()
        self.num_menuitem =len(self.driver.find_elements_by_xpath(self.menuitem_xpath))
        self.logger.info(str(self.num_menuitem))
        for item in range(2, 4):
            self.driver.find_element_by_xpath(self.menuitem_xpath + "[" + str(item) + "]").click()
            self.driver.find_element_by_xpath(self.menubutton_xpath).click()
        self.driver.quit()






