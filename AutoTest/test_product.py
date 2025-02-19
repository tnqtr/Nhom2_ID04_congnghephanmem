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
        inputUserName.send_keys("manager1")
        time.sleep(1)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys("987654321manager1")
        time.sleep(1)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    # def test_1_list_products(self):
    #     self.driver.get("http://127.0.0.1:8000/login/products/product.html")
    #     time.sleep(3)
    #     self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_2_add_product(self):
        self.driver.get("http://127.0.0.1:8000/login/products/product.html")
        time.sleep(3)
        self.driver.get("http://127.0.0.1:8000/login/products/add-product.html")
        time.sleep(3)
        self.driver.find_element(By.NAME, value="maSP").send_keys("SP1")
        self.driver.find_element(By.NAME, value="maLoaiSP").send_keys("L01")
        self.driver.find_element(By.NAME, value="tenSP").send_keys("Test Product")
        self.driver.find_element(By.NAME, value="trongLuong").send_keys("10")
        self.driver.find_element(By.NAME, value="tienCong").send_keys("1000")
        self.driver.find_element(By.NAME, value="tienDa").send_keys("500")
        self.driver.find_element(By.NAME, value="barcodeSP").send_keys("123456789")
        self.driver.find_element(By.NAME, value="barcodeSP").send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_3_edit_product(self):
        # Ensure the product exists before editing
        self.driver.get("http://127.0.0.1:8000/login/products/product.html") 
        time.sleep(3)
        dropdown_button = self.driver.find_element(By.XPATH, f"//td[text()='SP1']/following-sibling::td//i[@class='bi bi-three-dots-vertical']")
        dropdown_button.click()
        time.sleep(1)

        # Chọn mục "Sửa"
        edit_button = self.driver.find_element(By.XPATH, f"//td[text()='SP1']/following-sibling::td//a[contains(@href, 'edit-product')]")
        edit_button.click()
        time.sleep(3)
        self.driver.get("http://127.0.0.1:8000/login/products/edit-product.html/SP1/")
        time.sleep(3)
        input_maLoaiSP = self.driver.find_element(By.NAME, "maLoaiSP")
        input_maLoaiSP.clear()
        input_maLoaiSP.send_keys("L01")

        input_tenSP = self.driver.find_element(By.NAME, "tenSP")
        input_tenSP.clear()
        input_tenSP.send_keys("Updated Product")

        input_trongLuong = self.driver.find_element(By.NAME, "trongLuong")
        input_trongLuong.clear()
        input_trongLuong.send_keys("15")

        input_tienCong = self.driver.find_element(By.NAME, "tienCong")
        input_tienCong.clear()
        input_tienCong.send_keys("1500")

        input_tienDa = self.driver.find_element(By.NAME, "tienDa")
        input_tienDa.clear()
        input_tienDa.send_keys("750")

        input_barcodeSP = self.driver.find_element(By.NAME, "barcodeSP")
        input_barcodeSP.clear()
        input_barcodeSP.send_keys("987654321")
    
    # Nhấn Enter để submit form
        input_barcodeSP.send_keys(Keys.RETURN)  
        time.sleep(3)
              
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_4_delete_product(self):
        self.driver.get("http://127.0.0.1:8000/login/products/product.html")
        time.sleep(3)
        dropdown_button = self.driver.find_element(By.XPATH, f"//td[text()='SP1']/following-sibling::td//i[@class='bi bi-three-dots-vertical']")
        dropdown_button.click()
        time.sleep(1)

        # Chọn mục "Xóa"
        delete_button = self.driver.find_element(By.XPATH, f"//td[text()='SP1']/following-sibling::td//a[contains(@href, 'delete-product')]")
        delete_button.click()
        time.sleep(3)
        self.driver.get("http://127.0.0.1:8000/login/products/delete-product/SP1/")
        time.sleep(3)
        self.driver.find_element(By.NAME, value="delete_button").click()
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()