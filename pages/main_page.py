from selene import browser, have


class MainPage:
    def open(self):
        browser.open("https://github.com")
        return self

    def button_sign_in_desktop(self):
        browser.element(".HeaderMenu-link--sign-in").click()

    def button_sign_in_mobile(self):
        browser.element(".Button--link").click()
        browser.element(".HeaderMenu-link--sign-in").click()

    def should_have_sign_form(self):
        browser.should(have.url("https://github.com/login"))

    def should_have_text(self):
        browser.element(".auth-form-header").element("h1").should(have.text("Sign in to GitHub"))


main_page = MainPage()
