from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    choose_element,
    open_add_property_object,
    open_auth_page,
    open_choose_element,
    open_section,
    sign_in,
    wait_and_close_modals,
    wait_auth_page,
    wait_balance_transfer_tab,
    wait_main_page,
)


@allure.label('owner', 'a.seregin')
@allure.label('component', 'DIT')
@allure.epic('Mosgorzakaz Interface')
@allure.story('Главная страница')
@allure.title('Заведение нового объекта имущества в ПНБ и открытие АРМ ПНБ ')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_new_property_object_pnb(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    username = request.config.option.username

    app = make_app(browser, device_type)

    open_auth_page(app)
    wait_auth_page(app)

    sign_in(app, username, request.config.option.password)
    wait_main_page(app, username)

    wait_and_close_modals(app)

    open_section(app, 'Передача на баланс', 'АРМ')
    wait_balance_transfer_tab(app, username)

    open_add_property_object(app)

    open_choose_element(app, 'Наименование:')
    choose_element(app, 'Наименование:', 'ДИТ_автотест')

    open_choose_element(app, 'Объект АИП:')
    choose_element(app, 'Объект АИП:', 'ОВД района Сокол . Типовой проект с переработкой.')
