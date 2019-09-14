# -*- coding: utf-8 -*-


from locators import MainPageLocators
from locators import LoginPageLocators
from locators import RegisterPageLocator
from locators import  ForgetPasswordLocators
from locators import ResetPasswordLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def _verify_page(self):
        return

class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def _verify_page(self):
        assert "Oficjalna strona Wizz Air" in self.driver.title

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))

    def click_login_button(self):
        """Triggers the search"""
        el = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        el.click()


class ForgetPassword(BasePage):
    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ForgetPasswordLocators.RESET_EMAIL_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ForgetPasswordLocators.RESET_EMAIL_BUTTON))

    def click_reset_button(self):
        el = self.driver.find_element(*ForgetPasswordLocators.RESET_EMAIL_BUTTON)
        el.click()

    def fill_email_field(self, email):
        el = self.driver.find_element(*ForgetPasswordLocators.EMAIL_FIELD)
        el.send_keys(email)


class ResetPassword(BasePage):
    def _verify_page(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(ResetPasswordLocators.CONFIRM_BUTTON))
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(ResetPasswordLocators.CONFIRM_BUTTON))

    def click_confirm_button(self):
        el = self.driver.find_element(*ResetPasswordLocators.CONFIRM_BUTTON)
        el.click()

    def check_if_proper_message_is_displayed(self):
        message = self.driver.find_element(*ResetPasswordLocators.BODY)
        if message.is_displayed():
            return message.get_attribute('innerText')


class LoginPage(BasePage):

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))

    def click_register_button(self):
        el = self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON)
        el.click()

    def click_login_button(self):
        el = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        el.click()

    def check_if_proper_email_error_is_displayed(self):
        error = self.driver.find_element(*LoginPageLocators.ERROR_NOTICE_EMAIL)
        if error.is_displayed():
            return error.get_attribute('innerText')

    def check_if_proper_password_error_is_displayed(self):
        error = self.driver.find_element(*LoginPageLocators.ERROR_NOTICE_PASSWORD)
        if error.is_displayed():
            return error.get_attribute('innerText')

    def click_forget_password_button(self):
        el = self.driver.find_element(*LoginPageLocators.FORGET_PASSWORD_BUTTON)
        el.click()


class RegisterPage(BasePage):

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RegisterPageLocator.REGISTER_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RegisterPageLocator.REGISTER_BUTTON))

    def fill_name_field(self, name):
        el = self.driver.find_element(*RegisterPageLocator.FIRST_NAME_FIELD)
        el.send_keys(name)

    def fill_last_name_field(self, last_name):
        el = self.driver.find_element(*RegisterPageLocator.LAST_NAME_FIELD)
        el.send_keys(last_name)

    def fill_mobile_number_field(self, mobile_number):
        el = self.driver.find_element(*RegisterPageLocator.MOBILE_NUMBER_FIELD)
        el.send_keys(mobile_number)

    def fill_email_field(self, email):
        el = self.driver.find_element(*RegisterPageLocator.EMAIL_FIELD)
        el.send_keys(email)

    def fill_password_field(self, password):
        el = self.driver.find_element(*RegisterPageLocator.PASSWORD_FIELD)
        el.send_keys(password)

    def click_register_button(self):
        el = self.driver.find_element(*RegisterPageLocator.REGISTER_BUTTON)
        el.click()

    def click_private_policy_checkbox(self):
        el = self.driver.find_element(*RegisterPageLocator.PRIVATE_POLICY_CHECKBOX)
        el.click()

    def click_gender_button(self, gender):
        if gender =='male':
            el = self.driver.find_element(*RegisterPageLocator.MALE_BUTTON)
            self.driver.execute_script("arguments[0].click()",el)
        else:
            el = self.driver.find_element(*RegisterPageLocator.FEMALE_BUTTON)
            self.driver.execute_script("arguments[0].click()", el)

    def click_country_button(self):
        el = self.driver.find_element(*RegisterPageLocator.COUNTRY_FIELD)
        el.click()

    def choose_country(self, country):

        self.click_country_button()
        country_to_choose = self.driver.find_element(*RegisterPageLocator.COUNTRY_LIST)
        countries = country_to_choose.find_elements_by_xpath("label")
        for label in countries:
            d = label.find_element_by_tag_name('strong')
            if d.get_attribute("innerText") == country:
                d.location_once_scrolled_into_view
                d.click()
                break

    def check_if_proper_email_error_is_displayed(self):
        error = self.driver.find_element(*RegisterPageLocator.ERROR_NOTICE_EMAIL)
        if error.is_displayed():
            return error.get_attribute('innerText')



