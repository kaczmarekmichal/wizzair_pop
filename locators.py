from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_BUTTON = (By.XPATH, "//button[@data-test='navigation-menu-signin']")


class LoginPageLocators(object):
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Rejestracja']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-test='loginmodal-signin']")
    ERROR_NOTICE_EMAIL = (
        By.XPATH, "//span[@class='rf-input__error__message']/span[text()='Nieprawidłowy adres e-mail']")
    ERROR_NOTICE_PASSWORD = (By.XPATH, "//span[@class='rf-input__error__message']/span[text()='Wpisz hasło']")
    FORGET_PASSWORD_BUTTON = (By.XPATH, "//button[text()=' Nie pamiętasz hasła? ']")


class ForgetPasswordLocators(object):
    EMAIL_FIELD = (By.XPATH, "// input[ @ placeholder = 'E-mail']")
    RESET_EMAIL_BUTTON = (
        By.XPATH,
        "//button[@class='rf-button rf-button--medium rf-button--full-width rf-button--primary gutter-bottom']")


class ResetPasswordLocators(object):
    CONFIRM_BUTTON = (By.XPATH,
                      "//button[@class='rf-button rf-button--medium rf-button--full-width rf-button--primary']")
    HEADER = (By.XPATH, "//strong[text()='Masz wiadomość!']")
    BODY = (By.XPATH,
            "//p[@class='gutter-top gutter-bottom']/p[text()='Na Twój adres e-mail wysłaliśmy instrukcje resetowania hasła i odzyskiwania konta.']")


class RegisterPageLocator(object):
    FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='Imię']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='Nazwisko']")
    MOBILE_NUMBER_FIELD = (By.XPATH, "//input[@name='phoneNumberValidDigits']")
    EMAIL_FIELD = (By.XPATH, "//input[@data-test='booking-register-email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@data-test='booking-register-password']")
    REGISTER_BUTTON = (By.XPATH, "//button[@data-test='booking-register-submit']")
    PRIVATE_POLICY_CHECKBOX = (By.XPATH, "//label[@for='registration-privacy-policy-checkbox']")
    FEMALE_BUTTON = (By.XPATH, "//label[@for='register-gender-female']")
    MALE_BUTTON = (By.XPATH, "//label[@for='register-gender-male']")
    COUNTRY_FIELD = (By.XPATH, "//input[@data-test='booking-register-country']")
    COUNTRY_LIST = (By.XPATH, "//div[@class='register-form__country-container__locations']")
    ERROR_NOTICE_EMAIL = (By.XPATH,
                          "//span[@class='rf-input__error__message']/span[text()='Nieprawidłowy adres e-mail']")
