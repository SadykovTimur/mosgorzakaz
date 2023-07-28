from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    close_add_object_aip_modal,
    open_add_object_aip_modal,
    open_auth_page,
    open_object_aip,
    open_section,
    sign_in,
    wait_and_close_modals,
    wait_auth_page,
    wait_main_page,
    wait_registry_object_aip_tab,
)


@allure.label('owner', 'a.seregin')
@allure.label('component', 'DIT')
@allure.epic('Mosgorzakaz Interface')
@allure.story('Главная страница')
@allure.title('Доступность добавления карточки объекта АИП')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_add_object_aip(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    username = request.config.option.username

    app = make_app(browser, device_type)

    open_auth_page(app)
    wait_auth_page(app)

    sign_in(app, username, request.config.option.password)
    wait_main_page(app, username)

    wait_and_close_modals(app)

    open_section(app, 'Реестры', 'Реестр объектов АИП (Новый)')
    wait_registry_object_aip_tab(app, username)

    open_add_object_aip_modal(app)
    close_add_object_aip_modal(app)

    open_object_aip(app)
