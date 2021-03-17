# seleniumWithDdt

```py
import os
import time
import unittest
# import HTML
from selenium import webdriver
from ddt import ddt, data, unpack, file_data
import yaml


@ddt
class tUnittestHtml(unittest.TestCase):
    fpn_chrome_driver = "F:\Mirror\Software\Google\Chrome\chromedriver_win32\chromedriver.exe"
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        print(f"This is setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("This is tearDownClass")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=self.fpn_chrome_driver)
        pass

    def tearDown(self) -> None:
        self.driver.quit()
        pass

    @data('marathon', 'python')
    def test_first_selenium(self, txt):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys(txt)
        self.driver.find_element_by_id("su").click()
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
```
