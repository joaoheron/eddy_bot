# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from eddy_bot.models.selenium_bot import SeleniumBot
import eddy_bot.vars

class InstagramSeleniumBot(SeleniumBot):

    def __init__(self, browser='firefox', mobile=False):
        SeleniumBot.__init__(self, browser, mobile)

    def login(self):
        self.driver.get('https://instagram.com/')
        time.sleep(randint(1250, 3000))

        if check_exists_by_xpath(self.driver, "//button[text()='Accept']"):
            print("No cookies")
        else:
            self.driver.find_element_by_xpath("//button[text()='Accept']").click()
            print("Accepted cookies")

        time.sleep(randint(1250, 3000))
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/div[3]/button[1]').click()
        print("Logging in...")
        time.sleep(randint(1250, 3000))
        username_field = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input')
        username_field.send_keys(self.username)

        find_pass_field = (By.XPATH, '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input')
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(find_pass_field))

        pass_field = self.driver.find_element(*find_pass_field)
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(find_pass_field))
        pass_field.send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button').click()
        time.sleep(randint(1250, 3000))

    def comment(self):
        for profile in self.profiles:
            comment = self.random_comment

            self.driver.get(url)
            self.driver.implicitly_wait(1)

            self.driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
            time.sleep(2)

            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[1]/button').click()
            time.sleep(2)

            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button').click()

            if check_exists_by_xpath(bot, '/html/body/div[1]/section/main/section/div'):
                print("skiped")
                return run.comment(random_comment())

            find_comment_box = (
                By.XPATH, '/html/body/div[1]/section/main/section/div[1]/form/textarea')
            WebDriverWait(bot, 50).until(
                EC.presence_of_element_located(find_comment_box))
            comment_box = self.driver.find_element(*find_comment_box)
            WebDriverWait(bot, 50).until(
                EC.element_to_be_clickable(find_comment_box))
            comment_box.click()
            time.sleep(1)
            comment_box.send_keys(comment)

            find_post_button = (
                By.XPATH, '/html/body/div[1]/section/main/section/div/form/button')
            WebDriverWait(bot, 50).until(
                EC.presence_of_element_located(find_post_button))
            post_button = self.driver.find_element(*find_post_button)
            WebDriverWait(bot, 50).until(
                EC.element_to_be_clickable(find_post_button))
            post_button.click()

            time.sleep(5)

    def random_comment():
        comment = random.choice(self.comments)
        return comment