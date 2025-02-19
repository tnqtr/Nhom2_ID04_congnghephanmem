import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class CustomerTests(unittest.TestCase):

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

    def test_1_timKiemSP(self):
        self.driver.get("http://127.0.0.1:8000/login/customers/customer.html")
        time.sleep(3)
        self.driver.find_element(By.NAME, value="q").send_keys("Nguyen Thi A")
        time.sleep(1)
        self.driver.find_element(By.NAME, value="q").send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_2_add_customer(self):
        self.driver.get("http://127.0.0.1:8000/login/customers/customer.html")
        time.sleep(3)
        self.driver.get("http://127.0.0.1:8000/login/customers/add-customer.html")
        time.sleep(3)
        self.driver.find_element(By.NAME, value="maKH").send_keys("KH1")
        self.driver.find_element(By.NAME, value="hoTen").send_keys("Test Customer")
        self.driver.find_element(By.NAME, value="soDT").send_keys("0123456789")
        self.driver.find_element(By.NAME, value="email").send_keys("testcustomer@example.com")
        self.driver.find_element(By.NAME, value="diemTichLuy").send_keys("100")
        self.driver.find_element(By.NAME, value="email").send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_3_edit_customer(self):
        self.driver.get("http://127.0.0.1:8000/login/customers/customer.html")
        
        self.driver.get("http://127.0.0.1:8000/login/customers/edit-customer.html/KH1/")
        time.sleep(3)
        input_tenKH = self.driver.find_element(By.NAME, "hoTen")
        input_tenKH.clear()
        input_tenKH.send_keys("Updated Customer")

        input_soDienThoai = self.driver.find_element(By.NAME, "soDT")
        input_soDienThoai.clear()
        input_soDienThoai.send_keys("0987654321")

        input_email = self.driver.find_element(By.NAME, "email")
        input_email.clear()
        input_email.send_keys("updatedcustomer@example.com")
    
        input_email.send_keys(Keys.RETURN)  
        time.sleep(3)
              
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_4_delete_customer(self):
        self.driver.get("http://127.0.0.1:8000/login/customers/customer.html")
        time.sleep(3)
        
        self.driver.get("http://127.0.0.1:8000/login/customers/delete-customer/KH1/")
        time.sleep(3)
        self.driver.find_element(By.NAME, value="delete_button").click()
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()