
# Assignment

This Assignment consists of Selenium and Appium Automation tasks assigned.

## Pre-requisites

 - [Android Studio](https://developer.android.com/studio)
 - [Android SDK tools](https://guides.codepath.com/android/installing-android-sdk-tools)
 - [Appium server](https://appium.io/)
 - [Allure](https://docs.qameta.io/allure/) (for Reporting)
## Appendix

- Before running the scripts, user should install the requirements from requirements file.
- Developer options should be enabled in the Android device. 
## Description

Selenium Automation:
- In this, We are navigating to the weather report link for getting the temperature details of the particular city and comparing with the API result for same city.
- We have covered the scenarios in which we will get success once the temperature of both the results varies in same variance otherwise we will get the matcher exception.
Test Case Coverage:
- Test to get the temperature for the city and if city name is Invalid, Result will be City not found.
- Test to verify the result from both sources lies in same variance range.
Running Test Script:
- We have Find_Weather_Report.py which takes input as JSON with city names and variance (in %)
- We compare results from both API and UI and displays the resultant.
- Command : Under Assignment- python Selenium_assignment/Find_Weather_Report.py

Appium Automation:
- In this, We will first launch tha Appium server.
- We will install and launch the application from play store and will login using login type as twitter.
Test Case Coverage:
- Test to search and install the application using app name.
- Test to open the application and login with login type as twitter.
Running Test Script:
- We have LaunchApp.py file which have the scripts for running the Mobile automation.
- We have to connect to the system and mobile using USB.
- Command: Under Assignment- pytest Appium_Assignment/LaunchApp.py --alluredir=./allure-results --clean
 After successful script run execute command for report: allure serve allure-results/
## 🔗 Links
https://github.com/Keshavgoyal788/Automation
  