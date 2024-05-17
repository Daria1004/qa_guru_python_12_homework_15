"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""

from pages.main_page import main_page
from tests.conftest import desktop_only, mobile_only


@desktop_only
def test_github_desktop(browser_setup):
    main_page.open()
    main_page.button_sign_in_desktop()
    main_page.should_have_sign_form()
    main_page.should_have_text()


@mobile_only
def test_github_mobile(browser_setup):
    main_page.open()
    main_page.button_sign_in_mobile()
    main_page.should_have_sign_form()
    main_page.should_have_text()
