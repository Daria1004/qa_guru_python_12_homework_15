import pytest
from selene import browser

@pytest.fixture
def desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()

@pytest.fixture
def mobile():
    browser.config.window_width = 430
    browser.config.window_height = 932

    yield

    browser.quit()


@pytest.fixture(params=[("desktop", 1920, 1080), ("desktop", 1366, 768), ("mobile", 430, 932), ("mobile", 393, 852)])
def browser_setup(request):
    browser.config.window_width = request.param[1]
    browser.config.window_height = request.param[2]

    yield request.param[0]


mobile_only = pytest.mark.parametrize("browser_setup", [("mobile", 430, 932), ("mobile", 393, 852)], indirect=True)
desktop_only = pytest.mark.parametrize("browser_setup", [("desktop", 1920, 1080), ("desktop", 1366, 768)], indirect=True)
