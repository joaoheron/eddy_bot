import time
from random import randint, choice

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

from eddy_bot.models.social_media_bot import SocialMediaBot


class SeleniumBot(SocialMediaBot):

    def __init__(self, browser='firefox', mobile=False, credentials_path=vr.tags_path, tags_path=vr.tags_path, profiles_path=vr.profiles_path, comments_path=vr.comments_pat):
        SocialMediaBot.__init__(self, credentials_path, tags_path, profiles_path, comments_path)
        self.browser = browser
        self.driver = (self.build_firefox_driver() if browser == 'firefox' else self.build_chrome_driver())

    def exit(self):
        self.driver.quit()

    # Drivers building

    def build_firefox_driver(self, timeout=30, mobile=True):
        """This method builds options for Mozille Firefox Driver.

        :param headless: Indicates if the driver will be headless (hidden).
        :type headless: str
        """
        print('Building Gecko Driver...')
        user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", user_agent)
        driver = webdriver.Firefox(profile, executable_path=vr.geckodriver_path)
        driver.set_window_size(500, 950)
        return driver

    def build_chrome_driver(self, timeout=30, mobile=True):
        """This method builds options for Chrome Driver.

        :param headless: Indicates if the driver will be headless (hidden).
        :type headless: str
        """
        print('Building Chrome Driver...')
        driver = webdriver.Chrome(chrome_options=self._build_chrome_options(), executable_path=vr.chromedriver_path)
        driver.set_window_size(500, 950)
        return driver

    def _build_chrome_options(self, headless=True):
        """This method builds options for Chrome Driver.

        :param headless: Indicates if the driver will be headless (hidden).
        :type headless: str
        """
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--verbose')
        chrome_options.add_experimental_option("prefs", {
                "download.default_directory": f'{var.download_dir}',
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing_for_trusted_sources_enabled": False,
                "safebrowsing.enabled": False
        })
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-software-rasterizer')
        chrome_options.add_argument('--headless=' + str(headless))
        return chrome_options

    # Common Webdriver Methods

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return True

        return False

    def wait(self):
        time.sleep(randint(2, 3))
