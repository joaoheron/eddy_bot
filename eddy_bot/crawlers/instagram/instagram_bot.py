from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from eddy_bot.models.selenium_bot import SeleniumBot
from eddy_bot.utils import pick_random_resource


class InstagramSeleniumBot(SeleniumBot):

    def __init__(self, **kwargs):
        SeleniumBot.__init__(self, kwargs)
        self.base_url = 'https://instagram.com/'

    # def like_tag_post()
    # def like_profile_post()
    # def like_post()

    # def comment_profile_post(like=True) # profile no singular
    # def comment_tag(like=True)
    # def comment_post()

    # def follow_profile
    # def follow_profile_followers(n_followers)
    # def follow_profile_following(n_following)
    
    # def send_message_to_profile()

    def login(self):
        self.driver.get(self.base_url)
        self.wait()

        if self.check_exists_by_xpath("//button[text()='Accept']"):
            print("No cookies")
        else:
            self.driver.find_element_by_xpath("//button[text()='Accept']").click()
            print("Accepted cookies")

        self.wait()
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/div[3]/button[1]').click()
        print("Logging in...")
        self.wait()
        username_field = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input')
        username_field.send_keys(self.username)

        find_pass_field = (By.XPATH, '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input')
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(find_pass_field))

        pass_field = self.driver.find_element(*find_pass_field)
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(find_pass_field))
        pass_field.send_keys(self.password)

        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button').click()
        self.wait()

    def comment_profiles_posts(self, n_posts=3):
        """

        """
        # Iterate over all instagram profiles stored on vars.profile_path
        for profile in self.profiles:
            comment = pick_random_resource(self.comments)

            self.driver.get(self.base_url + profile)
            self.driver.implicitly_wait(1)

            self.driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
            posts_xpaths = self.get_top_profiles_posts(n_posts)

            for xp in posts_xpaths:
                self.wait()

                find_post_div = (By.XPATH, xp)
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(find_post_div))
                self.driver.find_element_by_xpath(xp).click()

                # Click to comment
                self.wait()
                self.driver.execute_script("window.scrollTo(0, window.scrollY + 600)")
                find_comments_button = (By.XPATH, '/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[2]/button')
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(find_comments_button))
                comments_button = self.driver.find_element(*find_comments_button)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(find_comments_button))
                comments_button.click()

                # Write comment
                find_comment_box = (By.XPATH, '/html/body/div[1]/section/main/section/div/form/textarea')
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(find_comment_box))
                comment_box = self.driver.find_element(*find_comment_box)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(find_comment_box))
                comment_box.send_keys(comment)

                # Post comment
                find_post_button = (By.XPATH, '/html/body/div[1]/section/main/section/div/form/button')
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(find_post_button))
                post_button = self.driver.find_element(*find_post_button)
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(find_post_button))
                post_button.click()
                self.wait()

                self.driver.get(self.base_url + profile)
                self.driver.implicitly_wait(1)
                self.driver.execute_script("window.scrollTo(0, window.scrollY + 300)")


    def get_top_profiles_posts(self, n_posts=3):
        base_top_posts = '/html/body/div[1]/section/main/div/div[4]/article/div[1]/div/div[1]/div'
        posts = []
        for i in range(n_posts):
            posts.append(f'{base_top_posts}[{str(i + 1)}]/a/div/div[2]')
        return posts
