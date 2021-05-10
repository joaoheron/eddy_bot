from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import eddy_bot.vars as vr 


class SeleniumBot():

    def __init__(self, browser='firefox', mobile=False):
        self.browser = browser
        self.username, self.password = self.get_credentials()
        self.tags = self.get_resource(vr.tags_path)
        self.profiles = self.get_resource(vr.profiles_path)
        self.comments = self.get_resource(vr.comments_path)
        self.driver = (self.build_firefox_driver() if browser == 'firefox' else self.build_chrome_driver())

    def get_credentials(self):
        with open(vr.credentials_path, 'r') as f:
            tagsl = [line.strip() for line in f]
        return tagsl[0], tagsl[1]
        
    def get_resource(self, path):
        with open(path, 'r') as f:
            resources = [line.strip() for line in f]
        return resources

    def exit(self):
        self.driver.quit()

    # Drivers building

    def build_chrome_driver(self, timeout=30):
        """This method builds options for Chrome Driver.

        :param headless: Indicates if the driver will be headless (hidden).
        :type headless: str
        """
        print('Building Chrome Driver...')
        self.driver = webdriver.Chrome(chrome_options=self._build_chrome_options(), executable_path=vr.chromedriver_path)
        self.driver.set_window_size(500, 950)
        return self.driver

    def build_firefox_driver(self, timeout=30):
        """This method builds options for Mozille Firefox Driver.

        :param headless: Indicates if the driver will be headless (hidden).
        :type headless: str
        """
        print('Building Gecko Driver...')
        user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", user_agent)
        self.driver = webdriver.Firefox(profile, executable_path=vr.geckodriver_path)
        self.driver.set_window_size(500, 950)
        return self.driver

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
