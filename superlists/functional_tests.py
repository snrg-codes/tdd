from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_myTest(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('successfully!', self.browser.title)

if __name__ == '__main__':
    unittest.main()