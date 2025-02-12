import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class WarrantyTests(unittest.TestCase):

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

    def test_1_list_warranties(self):
        self.driver.get("http://127.0.0.1:8000/login/warranty/warranty.html")
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_2_add_warranty(self):
        self.driver.get("http://127.0.0.1:8000/login/warranty/add-warranty.html")
        time.sleep(3)
        self.driver.find_element(By.NAME, value="maBH").send_keys("BH1")
        self.driver.find_element(By.NAME, value="donHangLienKet").send_keys("DH1")
        self.driver.find_element(By.NAME, value="donHangLienKet").send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_3_edit_warranty(self):
        self.driver.get("http://127.0.0.1:8000/login/warranty/warranty.html")
        time.sleep(3)
        
        # Nhấn vào menu ba chấm
        dropdown_button = self.driver.find_element(By.XPATH, "//tr[td[text()='BH1']]//i[@class='bi bi-three-dots-vertical']")
        dropdown_button.click()
        time.sleep(1)
        
        # Chọn mục "Sửa"
        edit_button = self.driver.find_element(By.XPATH, "//tr[td[text()='BH1']]//a[contains(@href, 'edit-warranty')]")
        edit_button.click()
        time.sleep(3)

        self.driver.get("http://127.0.0.1:8000/login/warranty/edit-warranty.html/BH1/")
        time.sleep(3)
        
        input_donHangLienKet = self.driver.find_element(By.NAME, "donHangLienKet")
        input_donHangLienKet.clear()
        input_donHangLienKet.send_keys("L05")
        
        # Nhấn Enter để submit form
        input_donHangLienKet.send_keys(Keys.RETURN)  
        time.sleep(3)
              
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_4_delete_warranty(self):
        self.driver.get("http://127.0.0.1:8000/login/warranty/warranty.html")
        time.sleep(3)
        
        # Nhấn vào menu ba chấm
        dropdown_button = self.driver.find_element(By.XPATH, "//tr[td[text()='BH1']]//i[@class='bi bi-three-dots-vertical']")
        dropdown_button.click()
        time.sleep(1)
        
        # Chọn mục "Xóa"
        delete_button = self.driver.find_element(By.XPATH, "//tr[td[text()='BH1']]//a[contains(@href, 'delete-warranty')]")
        delete_button.click()
        time.sleep(3)
        
        self.driver.get("http://127.0.0.1:8000/login/warranty/delete-warranty.html/BH1/")
        time.sleep(3)
        self.driver.find_element(By.NAME, value="delete_button").click()
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()