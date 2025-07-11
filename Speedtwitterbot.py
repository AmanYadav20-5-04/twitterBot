from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'start-text'))
        ).click()

        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'download-speed'))
        )
        self.down = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text)

    def tweet_at_provider(self, user, password, message):
        self.driver.get("https://x.com/login")

        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.NAME, 'text'))
            ).send_keys(user, Keys.ENTER)

            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            ).send_keys(password, Keys.ENTER)

            tweet_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Tweet text']"))
            )
            tweet_box.click()
            tweet_box.send_keys(message)

            tweet_button = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']")
            tweet_button.click()

        except Exception as e:
            print("Error during Twitter automation:", e)

    def close(self):
        self.driver.quit()
