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

    def test_1_list_discounts(self):
        self.driver.get("http://127.0.0.1:8000/login/discounts/discount.html")
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_2_add_discount(self):
        self.driver.get("http://127.0.0.1:8000/login/discounts/add-discount.html")
        time.sleep(3)
        self.driver.find_element(By.NAME, value="maKM").send_keys("KM1")
        self.driver.find_element(By.NAME, value="moTa").send_keys("Test Discount")
        self.driver.find_element(By.NAME, value="ngayBatDau").send_keys("2132025")
        self.driver.find_element(By.NAME, value="ngayKetThuc").send_keys("2202025")
        self.driver.find_element(By.NAME, value="tyLeChietKhau").send_keys("10")
        self.driver.find_element(By.NAME, value="tyLeChietKhau").send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_3_edit_discount(self):
        self.driver.get("http://127.0.0.1:8000/login/discounts/discount.html")
        time.sleep(3)
        dropdown_button = self.driver.find_element(By.XPATH, f"//td[text()='KM1']/following-sibling::td//i[@class='bi bi-three-dots-vertical']")
        dropdown_button.click()
        time.sleep(1)

        # Chọn mục "Sửa"
        edit_button = self.driver.find_element(By.XPATH, f"//td[text()='KM1']/following-sibling::td//a[contains(@href, 'edit-discount')]")
        edit_button.click()
        time.sleep(3)
        self.driver.get("http://127.0.0.1:8000/login/discounts/edit-discount.html/KM1/")
        time.sleep(3)
        input_moTa = self.driver.find_element(By.NAME, "moTa")
        input_moTa.clear()
        input_moTa.send_keys("Updated Discount")

        input_ngayBatDau = self.driver.find_element(By.NAME, "ngayBatDau")
        input_ngayBatDau.clear()
        input_ngayBatDau.send_keys("2132025")

        input_ngayKetThuc = self.driver.find_element(By.NAME, "ngayKetThuc")
        input_ngayKetThuc.clear()
        input_ngayKetThuc.send_keys("2202025")

        input_tyLeChietKhau = self.driver.find_element(By.NAME, "tyLeChietKhau")
        input_tyLeChietKhau.clear()
        input_tyLeChietKhau.send_keys("15")
    
        # Nhấn Enter để submit form
        input_tyLeChietKhau.send_keys(Keys.RETURN)  
        time.sleep(3)
              
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def test_4_delete_discount(self):
        self.driver.get("http://127.0.0.1:8000/login/discounts/discount.html")
        time.sleep(3)
        dropdown_button = self.driver.find_element(By.XPATH, f"//td[text()='KM1']/following-sibling::td//i[@class='bi bi-three-dots-vertical']")
        dropdown_button.click()
        time.sleep(1)

        # Chọn mục "Xóa"
        delete_button = self.driver.find_element(By.XPATH, f"//td[text()='KM1']/following-sibling::td//a[contains(@href, 'delete-discount')]")
        delete_button.click()
        time.sleep(3)
        self.driver.get("http://127.0.0.1:8000/login/discounts/delete-discount/KM1/")
        time.sleep(3)
        self.driver.find_element(By.NAME, value="delete_button").click()
        time.sleep(3)
        self.assertIn("Jewelry Store| Thống kê", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()