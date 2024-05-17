"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from pages.main_page import main_page


def test_github_desktop(desktop):
    main_page.open()
    main_page.button_sign_in_desktop()
    main_page.should_have_sign_form()
    main_page.should_have_text()


def test_github_mobile(mobile):
    main_page.open()
    main_page.button_sign_in_mobile()
    main_page.should_have_sign_form()
    main_page.should_have_text()
