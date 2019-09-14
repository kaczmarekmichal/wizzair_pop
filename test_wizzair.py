# _*_ coding: utf-8 _*_
import unittest
from selenium import webdriver
import test_data
from pages.pages import MainPage
from pages.pages import LoginPage
from pages.pages import RegisterPage
from pages.pages import ForgetPassword
from pages.pages import ResetPassword


class WizzairTest(unittest.TestCase):

    def tearDown(self):
        self.driver.quit()

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#")
        main_page = MainPage(self.driver)
        main_page._verify_page()

    def test_wrong_email_register(self):

        main_page = MainPage(self.driver)
        main_page._verify_page()
        main_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page._verify_page()
        login_page.click_register_button()

        register_page = RegisterPage(self.driver)
        register_page._verify_page()
        register_page.fill_name_field(test_data.valid_name)
        register_page.fill_last_name_field(test_data.valid_surname)
        register_page.click_gender_button(test_data.sex)
        register_page.fill_mobile_number_field(test_data.mobile_phone)
        register_page.fill_email_field(test_data.email)
        register_page.fill_password_field(test_data.password)
        register_page.choose_country(test_data.country)
        register_page.click_private_policy_checkbox()
        register_page.click_register_button()
        error_text = register_page.check_if_proper_email_error_is_displayed()
        self.assertEqual(error_text, u'Nieprawidłowy adres e-mail')
        self.driver.save_screenshot('test_wrong_email_register.png')

    def test_empty_login(self):

        main_page = MainPage(self.driver)
        main_page._verify_page()
        main_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page._verify_page()
        login_page.click_login_button()
        email_error = login_page.check_if_proper_email_error_is_displayed()
        self.assertEqual(email_error, u'Nieprawidłowy adres e-mail')
        password_error = login_page.check_if_proper_password_error_is_displayed()
        self.assertEqual(password_error, u'Wpisz hasło')
        self.driver.save_screenshot('test_empty_login.png')

    def test_forget_password(self):
        main_page = MainPage(self.driver)
        main_page._verify_page()
        main_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page._verify_page()
        login_page.click_forget_password_button()

        forget_password_page = ForgetPassword(self.driver)
        forget_password_page._verify_page()
        forget_password_page.fill_email_field(test_data.email_reset_password)
        forget_password_page.click_reset_button()

        reset_password_page = ResetPassword(self.driver)
        reset_password_page._verify_page()
        message = reset_password_page.check_if_proper_message_is_displayed()
        self.assertEqual(message,
                         u'Na Twój adres e-mail wysłaliśmy instrukcje resetowania hasła i odzyskiwania konta.')

        self.driver.save_screenshot('test_forget_password.png')


if __name__ == '__main__':
    unittest.main()
