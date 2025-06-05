from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_myTest(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do lists', self.browser.title)
        header_text = self.browser.find_elements(By.TAG_NAME, 'h1')[0].text
        print(header_text)
        self.assertIn('To-Do lists', header_text)
        # <h1>To-Do lists</h1>

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Bu joyga yangi ishni qo\'shing'
        )

        inputbox.send_keys("Telefonga pul o'tkazish")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Telefonga pul o\'tkazish' for row in rows),
        )

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()