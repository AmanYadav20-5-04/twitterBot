"""High level automation utilities for running a speed test and tweeting."""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class InternetSpeedTwitterBot:
    """Bot that measures internet speed and tweets a complaint if needed."""

    def __init__(self, headless: bool = False, wait_timeout: int = 30):
        self.chrome_options = ChromeOptions()
        if headless:
            self.chrome_options.add_argument("--headless=new")
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = Chrome(options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, wait_timeout)
        self.down = 0.0
        self.up = 0.0

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
        )

    def get_internet_speed(self) -> None:
        """Run a speed test and store the results in ``self.down`` and ``self.up``."""
        logging.info("Opening speedtest.net")
        self.driver.get("https://www.speedtest.net")
        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "start-text"))
        ).click()

        logging.info("Running speed test...")
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "download-speed"))
        )
        self.down = float(
            self.driver.find_element(By.CLASS_NAME, "download-speed").text
        )
        self.up = float(
            self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        )
        logging.info("Speed test results - Down: %s Mbps, Up: %s Mbps", self.down, self.up)

    def tweet_at_provider(self, user: str, password: str, message: str) -> None:
        """Log in to Twitter and send a tweet with ``message``."""
        logging.info("Logging into Twitter...")
        self.driver.get("https://x.com/login")

        try:
            self.wait.until(EC.presence_of_element_located((By.NAME, "text"))).send_keys(user, Keys.ENTER)

            self.wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password, Keys.ENTER)

            tweet_box = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Tweet text']"))
            )
            tweet_box.click()
            tweet_box.send_keys(message)

            tweet_button = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']")
            tweet_button.click()
            logging.info("Tweet sent successfully")

        except Exception as e:
            logging.error("Error during Twitter automation: %s", e)

    def close(self) -> None:
        """Close the underlying browser."""
        logging.info("Closing browser")
        self.driver.quit()
