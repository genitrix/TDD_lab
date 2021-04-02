from selenium import webdriver
import unittest

# 把测试写成类，它继承unittest.TestCase；
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # 以test开头的任何方法都是测试方法
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")

        self.assertIn("To-Do",self.browser.title)

        self.fail("Finish the tests!")

if __name__ == "__main__":
    # unittest.main（）方法，
    # 它启动unittest测试运行器，
    # 它将自动在文件中寻找测试类和方法并运行它们。
    # 防止了在撰写本文时爆出多余的ResourceWarning信息。
    unittest.main(warnings = 'ignore')
browser = webdriver.Firefox()

# Edith has heard about a cool new online to-do app. She goes
# to check out its homepage
# browser.get("http://localhost:8000")

# She notice the page title and header mention to-do lists
# assert "TO-DO" in browser.title, "Browser title was" + browser.title

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box (Edith's hobby
# is typing fly-fishing lures)

# when she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect

# She visits that URL - her to-do list is still there

# Satisfied, she goes back to sleep

# browser.quit()