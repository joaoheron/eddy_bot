from os import getenv
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from eddy_bot.models.selenium_bot import SeleniumBot
from eddy_bot.utils import pick_random_resource
from eddy_bot.logger import logger

class InstagramSeleniumBot(SeleniumBot):
    """
        Instagram selenium bot class
    """
    button_text_accept = "//button[text()='Accept']"
    possible_base_profile_top_posts = [
        "/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div",
        "/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div",
        "/html/body/div[1]/section/main/div/div[4]/article/div[1]/div/div[1]/div"
    ]
    comments_button = "/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[2]/button"
    comment_box = "/html/body/div[1]/section/main/section/div/form/textarea"
    post_button = "/html/body/div[1]/section/main/section/div/form/button"

    def __init__(self, config_path: str, profiles: str):
        SeleniumBot.__init__(self, config_path, profiles)
        InstagramSeleniumBot.validate_environment(['INSTAGRAM_USER', 'INSTAGRAM_PASS'])
        self.base_url = "https://instagram.com/"
        self.possible_profile_top_posts_xpaths = self.get_possible_profile_top_posts_xpaths()

    def login(self):
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(randint(1, 2))

        if self.check_exists_by_xpath(InstagramSeleniumBot.button_text_accept):
            logger.info("No cookies")
        else:
            self.driver.find_element_by_xpath(InstagramSeleniumBot.button_text_accept).click()
            logger.info("Accepted cookies")

        self.driver.implicitly_wait(randint(1, 2))
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/div[3]/button[1]').click()
        logger.info("Logging in...")
        self.driver.implicitly_wait(randint(1, 2))
        username_field = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input')
        username_field.send_keys(getenv('INSTAGRAM_USER'))

        find_pass_field = (By.XPATH, '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input')
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(find_pass_field))

        pass_field = self.driver.find_element(*find_pass_field)
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(find_pass_field))
        pass_field.send_keys(getenv('INSTAGRAM_PASS'))

        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button').click()
        self.driver.implicitly_wait(randint(1, 2))

    def comment_profiles_posts(self, n_posts=3):
        """
        """
        for profile in self.profiles:
            comment = pick_random_resource(self.comments)

            self.driver.get(self.base_url + profile)
            self.driver.implicitly_wait(1)
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 300)")

            for possibles_xpaths in self.possible_profile_top_posts_xpaths:
                self.comment_profile_post(profile, possibles_xpaths, comment)

    def comment_profile_post(self, profile, possibles_xpaths, comment):
        """
        """
        self.driver.implicitly_wait(randint(1, 2))
        for xp in possibles_xpaths:
            try:
                ele = self.driver.find_element_by_xpath(xp)
                if ele is None:
                    continue

                ele.click()
                self.driver.implicitly_wait(randint(1, 2))
                self.driver.execute_script("window.scrollTo(0, window.scrollY + 600)")

                # Click to comment
                comments_button = self.driver.find_element_by_xpath(InstagramSeleniumBot.comments_button)
                comments_button.click()

                # Write comment
                comment_box = self.driver.find_element_by_xpath(InstagramSeleniumBot.comment_box)
                comment_box.send_keys(comment)

                # Post comment
                post_button = self.driver.find_element_by_xpath(InstagramSeleniumBot.post_button)
                post_button.click()
                self.driver.implicitly_wait(randint(1, 2))

                self.driver.get(self.base_url + profile)
                self.driver.implicitly_wait(randint(1, 2))
                self.driver.execute_script("window.scrollTo(0, window.scrollY + 300)")

                break
            except Exception:
                continue

    def follow(self):
        for p in self.profiles:
            logger.info(f'Following profile {p}')

    def unfollow(self):
        for p in self.profiles:
            logger.info(f'Unfollowing profile {p}')

    def get_possible_profile_top_posts_xpaths(self, n_posts=1):
        possible_profile_top_posts_xpaths = []
        for j in range(n_posts):

            posts_xpaths = []
            for xpath in InstagramSeleniumBot.possible_base_profile_top_posts:
                posts_xpaths.append(f'{xpath}[{str(j + 1)}]/a/div/div[2]')

            possible_profile_top_posts_xpaths.append(posts_xpaths)

        return possible_profile_top_posts_xpaths
