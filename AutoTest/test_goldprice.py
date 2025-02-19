import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class ProductTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/login/login/")
        self.login()

    def login(self):
        inputUserName = self.driver.find_element(By.NAME, value="username")
        inputUserName.send_keys("admin")
        time.sleep(1)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys("123456")
        time.sleep(1)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
    def test_add_goldprice(self):
        self.driver.get("http://127.0.0.1:8000/admin/JS_Manage/banggiavang/add/")
        time.sleep(3)
        self.driver.find_element(By.NAME, value="ngayCapNhat_0").send_keys("2025-02-13")
        self.driver.find_element(By.NAME, value="ngayCapNhat_1").send_keys("14:24:43")

        input_goldprice=self.driver.find_element(By.NAME, value="loaiVang")
        input_goldprice.clear()
        input_goldprice.send_keys("Vàng 18K")
        time.sleep(1)
        self.driver.find_element(By.NAME, value="giaMua").send_keys("1000000")
        self.driver.find_element(By.NAME, value="giaBan").send_keys("2000000")
        self.driver.find_element(By.NAME, value="donVi").send_keys("Tr.VND")
        self.driver.find_element(By.NAME, value="donVi").send_keys(Keys.RETURN)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()