from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import eddy_bot.vars

def enable_download_headless(browser, download_dir):
    """This method enables that a webdriver download files even if it's a headless webdriver.

    :param download_dir: Folder to store the downloads.
    :type download_dir: str
    """
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

def build_chrome_options(headless=True):
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
            "download.default_directory": 'vars.download',
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
    })
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--headless=' + str(headless))

    return chrome_options

def build_driver(timeout=30):
    """This method builds options for Chrome Driver.

    :param headless: Indicates if the driver will be headless (hidden).
    :type headless: str
    """
    print('Building Driver...')
    # build options
    chrome_options = build_chrome_options()
    # initialize webdriver
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=vars.chromedriver_path)
    # maximize window
    driver.maximize_window()

    return driver
        
def screenshot(driver, download_dir=vars.download_dir, filename=vars.filename, fileformat=None):
    """This method takes a Screenshot of the screen.

    :param driver: Selenium web driver.
    :type driver: str
    :param download_dir: Folder to store screenshot file.
    :type download_dir: str
    :param filename: Screenshot's file name.
    :type filename: str
    :param fileformat: Screenshot's file format.
    :type fileformat: str
    """
    if os.path.exists(download_dir + filename):
        os.remove(download_dir + filename)
    driver.save_screenshot(download_dir + filename)
    print('Screenshoted screen and saved file at ' + str(download_dir))

def comment():
    """This method comments 
    """
    print('comment')