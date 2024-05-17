"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from pages.main_page import main_page


def test_github_desktop(browser_setup):
    if browser_setup != "desktop":
        pytest.skip('Mobile version')
    else:
        main_page.open()
        main_page.button_sign_in_desktop()
        main_page.should_have_sign_form()
        main_page.should_have_text()


def test_github_mobile(browser_setup):
    if browser_setup != "mobile":
        pytest.skip('Desktop version')
    else:
        main_page.open()
        main_page.button_sign_in_mobile()
        main_page.should_have_sign_form()
        main_page.should_have_text()
