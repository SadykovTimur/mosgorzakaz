from typing import Callable
from uuid import uuid4

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    close_test_record,
    fill_test_record,
    open_auth_page,
    open_section,
    open_test_record,
    remove_test_record,
    sign_in,
    wait_and_close_modals,
    wait_auth_page,
    wait_main_page,
    wait_test_registry_tab,
)


@allure.label('owner', 'a.seregin')
@allure.label('component', 'DIT')
@allure.epic('Mosgorzakaz Interface')
@allure.story('Главная страница')
@allure.title('Добавление тестовой записи')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_test_registry(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    username = request.config.option.username
    record_name = f'Тест{uuid4().hex[:8]}'

    app = make_app(browser, device_type)

    open_auth_page(app)
    wait_auth_page(app)

    sign_in(app, username, request.config.option.password)
    wait_main_page(app, username)

    wait_and_close_modals(app)

    open_section(app, 'Администрирование', 'Тест страница')
    wait_test_registry_tab(app, username)

    open_test_record(app)
    fill_test_record(app, record_name)
    close_test_record(app, record_name)

    remove_test_record(app, username)
