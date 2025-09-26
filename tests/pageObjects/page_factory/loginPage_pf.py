# Page Locators
# Page Actions
# Webdriver - Init
# Custom Functions
# No Assertion here ( They are not Test cases)

from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.highlight = True

    # Page Locators

    locators = {
        'username': ('CSS', "#login-username"),
        'password': ('NAME', 'password'),
        'error_message': ('CSS', '#js-notification-box-msg'),
        'submit_button': ('XPATH', '//button[@id="js-login-btn"]')
    }

    def login_to_vwo(self, user, pwd):
        self.username.set_text(user)
        self.password.set_text(pwd)
        self.submit_button.click_button()

    def error_msg(self):
        return self.error_message.get_text()

