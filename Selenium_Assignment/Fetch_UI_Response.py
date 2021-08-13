import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options


class FetchUIResponse:

    def getTempFromUI(city_name):

        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')

            driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver", options=chrome_options)

            URL = "https://weather.com/"

            driver.get(URL)
            driver.maximize_window()

            search_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@placeholder= 'Search City or Postcode']")))

            search_input.click()
            search_input.send_keys(city_name)

            time.sleep(2)
            search_input.send_keys(Keys.ENTER)

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[@data-testid= 'TemperatureValue']"))).is_dispayed()
            except Exception as e1:
                search_input.send_keys(Keys.ENTER)

            try:
                temperature = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[@data-testid= 'TemperatureValue']")))
            except Exception as e2:
                print('City not found !!!')
                temperature = None

            if temperature is not None:
                print(f'Current temperature is (in Celcius) from UI: {temperature.text}')
                return temperature.text
            return None
        except Exception as e:
            print('Exception occured: ' + str(e))
