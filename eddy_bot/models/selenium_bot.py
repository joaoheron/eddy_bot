from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

from eddy_bot.models.social_media_bot import SocialMediaBot
from eddy_bot.logger import logger
import eddy_bot.vars as vr


class SeleniumBot(SocialMediaBot):

    def __init__(self, credentials_path: str, config_path: str, browser: str = 'firefox', mobile: bool = True, headless: bool = False, timeout: str = 30):
        SocialMediaBot.__init__(self, credentials_path, config_path)
        self.driver = (self.build_firefox_driver(mobile, headless, timeout) if browser == 'firefox' else self.build_chrome_driver(mobile, headless, timeout))

    def exit(self):
        self.driver.quit()

    # Drivers building

    def build_firefox_driver(self, mobile: bool = True, headless: bool = True, timeout: int = 30) -> webdriver:
        """This method builds options for Mozille Firefox Driver.

        :param headless: Indicates if the driver will be headless (hidden).
        :type headless: str
        """
        logger.info('Building Gecko Driver...')
        user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", user_agent)
        driver = webdriver.Firefox(profile, executable_path=vr.geckodriver_path)
        driver.set_window_size(500, 950)
        return driver

    def build_chrome_driver(self, mobile: str = True, headless: bool = True, timeout: int = 30) -> webdriver:
        """This method builds options for Chrome Driver.

        :param headless: Indicates if the driver will be headless (hidden).
        :type headless: str
        """
        logger.info('Building Chrome Driver...')
        driver = webdriver.Chrome(chrome_options=self._build_chrome_options(), executable_path=vr.chromedriver_path)
        driver.set_window_size(500, 950)
        return driver

    def _build_chrome_options(self, headless: bool = True, download_dir: str = vr.download_dir) -> Options:
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
                "download.default_directory": f'{download_dir}',
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

    def check_exists_by_xpath(self, xpath: str):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return True

        return False
