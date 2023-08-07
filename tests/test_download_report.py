from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from dit.qa.helpers.date_helper import today
from tests.steps import (
    check_download_report,
    choose_report,
    open_auth_page,
    open_section,
    sign_in,
    wait_and_close_modals,
    wait_auth_page,
    wait_main_page,
    wait_reports_tab,
)


@allure.label('owner', 'a.seregin')
@allure.label('component', 'DIT')
@allure.epic('Mosgorzakaz Interface')
@allure.story('Главная страница')
@allure.title('Выгрузка отчёта из системы показателей')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_download_report(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    username = request.config.option.username

    app = make_app(browser, device_type)

    open_auth_page(app)
    wait_auth_page(app)

    sign_in(app, username, request.config.option.password)
    wait_main_page(app, username)

    wait_and_close_modals(app)

    open_section(app, 'Аналитика', 'Отчёты по показателям')
    wait_reports_tab(app, username)

    current_date = today()
    choose_report(app, username)

    check_download_report(app, current_date)
