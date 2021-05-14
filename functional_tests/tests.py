from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


# 把测试写成类，它继承unittest.TestCase；
class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_for_one_user(self):
        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    # add from demo code
    def test_can_start_a_list_for_one_user(self):
        # edith has heard about a cool new online to-do app.
        # she goes to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header metion to-do
        # lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # self.fail('Finsh the test!')

        # # She notice the page title and header mention to-do lists
        # self.assertIn("To-Do", self.browser.title)
        # header_text = self.browser.find_element_by_tag_name('h1').text
        # self.assertIn("To-Do", header_text)

    # 以test开头的任何方法都是测试方法
    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edit has heard about a cool new online to-do app. She goes
        # 1 to check out its homepage
        self.browser.get(self.live_server_url)
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She notices that her lists has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        # end 1

        # start page 6.18
        self.browser.quit()
        self.browser = webdriver.Firefox

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feather', page_text)
        self.assertIn('Buy milk', page_text)

        # satisfied, they both go back to sleep
        # end page 6.18

        # sleep is required
        # 刷新太快，需要sleep
        time.sleep(1)
        # get again
        # 对象会变，再获取一次
        # removed

        # inputbox = self.browser.find_element_by_id('id_new_item')
        # inputbox.send_keys("Use peacock feathers to make a fly")
        # inputbox.send_keys(Keys.ENTER)

        # time.sleep(10)

        # The page updates again, and now shows both items on her list

        # removed

        # self.wait_for_row_in_list_table("1: Buy peacock feathers")
        # self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")

        # self.assertEqual(
        #     inputbox.get_attribute('placeholder'),
        #     'Enter a to-do item'
        # )

        # She types "Buy peacock feathers" into a text box(Edith's hobby
        # is tying fly-fishing lures)

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        # self.assertIn(
        #     '2: Use peacock feathers to make a fly',
        #     [row.text for row in rows]
        # )

        # removed

        # self.fail("Finish the tests!")

        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     "New to-do item did not appear in table"
        # )
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     f"New to-do item did not appear in table. Contents were:\n{table.text}"
        # )

        # There is still  text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
    # unittest.main（）方法，
    # 它启动unittest测试运行器，
    # 它将自动在文件中寻找测试类和方法并运行它们。
    # 防止了在撰写本文时爆出多余的ResourceWarning信息。
    # browser = webdriver.Firefox()

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
