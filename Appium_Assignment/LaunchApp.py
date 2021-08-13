import unittest
from appium import webdriver
import allure


@allure.story('Appium Launch App Assignment')
@allure.feature('Test- Automation Framework python')
@allure.testcase('Login using Twitter in GameApp')
class LoginGameApp(unittest.TestCase):
    app_name = 'game.tv'
    email_id = 'tes1.auto1@gmail.com'
    password = 'game@twitter'

    def setUp(self):
        with allure.step('Launch Play Store'):
            desired_caps = {
                "platformName": 'Android',
                "noReset": "true",
                "fullReset": "false",
                "appPackage": "com.android.vending",
                "appActivity": "com.android.vending.AssetBrowserActivity",
            }
            self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)

    def teardown(self):
        self.driver.quit()

    def test_login_from_twitter(self):
        try:
            self.driver.implicitly_wait(20)
            with allure.step('Click on search box text'):
                search = self.driver.find_element_by_xpath(
                    "//*[@class='android.widget.TextView' and @resource-id='com.android.vending:id/0_resource_name_obfuscated' and @index='1' and @text='Search for apps & games']")
                search.click()
                self.driver.implicitly_wait(5)
            edit = self.driver.find_element_by_xpath(
                "//*[@class='android.widget.EditText' and @resource-id='com.android.vending:id/0_resource_name_obfuscated' and @index='0' and @text='Search for apps & games']")
            with allure.step('Edit the App name as ' + LoginGameApp.app_name):
                edit.send_keys(LoginGameApp.app_name)
            with allure.step('Click on search button in keyboard'):
                self.driver.keyevent(66)

            with allure.step('Wait for App to be displayed'):
                self.driver.implicitly_wait(5)
            install = self.driver.find_element_by_xpath("//*[@class='android.widget.Button' and @text='Install']")
            with allure.step('Click on install button on searched app'):
                install.click()

            with allure.step('Wait until installation completes'):
                self.driver.implicitly_wait(60)
            Open = self.driver.find_element_by_xpath("//*[@class='android.widget.Button' and @text='Open']")
            with allure.step('Click on Open button after successfull installation'):
                Open.click()

            with allure.step('Wait for installed app to be Open'):
                self.driver.implicitly_wait(5)
            twitter = self.driver.find_element_by_xpath(
                "//*[@class='android.widget.ImageView' and @content-desc='AuthoriseWithTwitter_593']")
            with allure.step('Login page is displayed for: ' + LoginGameApp.app_name + ' app'):
                twitter.is_displayed()
            with allure.step('Click on Twitter button after opening the app'):
                twitter.click()

            with allure.step('Wait for login option to appear after clicking on twitter icon'):
                self.driver.implicitly_wait(20)
            email = self.driver.find_element_by_xpath(
                "//*[@class='android.widget.EditText' and @resource-id= 'username_or_email']")
            with allure.step('Click on email edit box and enter the email_id as: ' + LoginGameApp.email_id):
                email.click()
                email.send_keys(LoginGameApp.email_id)
            password = self.driver.find_element_by_xpath(
                "//*[@class='android.widget.EditText' and @resource-id= 'password']")
            with allure.step('Click on password and enter the password as: ' + LoginGameApp.password):
                password.click()
                password.send_keys(LoginGameApp.password)
            login = self.driver.find_element_by_xpath(
                "//*[@class='android.widget.Button' and @resource-id='allow' and @text='Authorize app']")
            with allure.step('Click on login/Authorize App button'):
                login.click()

            self.driver.implicitly_wait(20)
        except Exception as e:
            print("Exception occured: " + str(e))
