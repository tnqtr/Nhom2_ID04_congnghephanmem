import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class DiscountTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/login/login/")
        self.login()

    def login(self):
        inputUserName = self.driver.find_element(By.NAME, value="username")
        inputUserName.send_keys("manager1")
        time.sleep(1)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys("987654321manager1")
        time.sleep(1)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def test_1_view_sell(self):
        self.driver.get("http://127.0.0.1:8000/login/sell/sell.html")
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_2_find_product(self):
        self.driver.get("http://127.0.0.1:8000/login/sell/sell.html")
        time.sleep(3)
        self.driver.find_element(By.NAME, value="q").send_keys("Nhẫn")
        time.sleep(1)
        self.driver.find_element(By.NAME, value="q").send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_3_add_to_order(self):
        self.driver.get("http://127.0.0.1:8000/login/sell/sell.html")
        time.sleep(3)
        add_button = self.driver.find_element(By.NAME, value="add")
        add_button.click()
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_4_payment(self):
        self.driver.get("http://127.0.0.1:8000/login/sell/sell.html")
        time.sleep(3)
        payment_button = self.driver.find_element(By.ID, value="payment")
        payment_button.click()
        time.sleep(1)
        self.driver.find_element(By.NAME, value="maHD").send_keys("HD01")
        self.driver.find_element(By.NAME, value="ngayTao").send_keys("20-02-2025")
        self.driver.find_element(By.NAME, value="maKH").send_keys("KH01")
        self.driver.find_element(By.NAME, value="maNV").send_keys("NV01")
        self.driver.find_element(By.NAME, value="tongTien").send_keys("100000000")
        self.driver.find_element(By.NAME, value="tongTien").send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()